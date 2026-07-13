"""
Unified docx-to-md conversion pipeline.
Three steps: pandoc text, zipfile images, path fixup + verification checklist.

Usage:
    python convert_all.py <source-directory>

Source directory should contain *_原文.docx files.
Images are extracted to media/<ep-number>/ per episode.
Output .md files are placed alongside the .docx files.
"""
import subprocess, os, glob, re, zipfile, shutil, sys

def safe_print(*args, **kwargs):
    """Print with GBK encoding fallback for problematic Unicode chars."""
    text = ' '.join(str(a) for a in args)
    try:
        print(text, **kwargs)
    except UnicodeEncodeError:
        print(text.encode('gbk', errors='replace').decode('gbk'), **kwargs)


def safe_name(path):
    """Return basename sanitized for GBK terminal output."""
    name = os.path.basename(path)
    try:
        name.encode('gbk')
        return name
    except UnicodeEncodeError:
        return name.encode('gbk', errors='replace').decode('gbk')


def main():
    SRC = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    PANDOC = r'C:\Users\ASUS\AppData\Local\Pandoc\pandoc'

    docx_files = sorted(glob.glob(os.path.join(SRC, '*_原文.docx')))
    if not docx_files:
        print(f"No *_原文.docx files found in {SRC}")
        return
    print(f"Found {len(docx_files)} docx files")

    # ── Step 1: Pandoc text conversion ──
    print("\n=== Step 1: Pandoc text conversion ===")
    for f in docx_files:
        out_md = f.replace('_原文.docx', '.md')
        if os.path.exists(out_md):
            safe_print(f"  SKIP (exists): {safe_name(out_md)}")
            continue
        safe_print(f"  Converting: {safe_name(f)}")
        subprocess.run(
            [PANDOC, f, '-f', 'docx', '-t', 'gfm', '--wrap=none', '-o', out_md],
            check=True
        )

    md_files = sorted(glob.glob(os.path.join(SRC, '*.md')))
    print(f"  -> {len(md_files)} markdown files (expect {len(docx_files)})")

    # ── Step 2: Extract images from docx zip ──
    print("\n=== Step 2: Extract images from docx zip ===")
    total_extracted = 0
    for f in docx_files:
        basename = os.path.basename(f)
        ep_match = re.match(r'(\d+)', basename)
        if not ep_match:
            safe_print(f"  SKIP (no episode number): {basename}")
            continue
        ep = ep_match.group(1)
        media_dir = os.path.join(SRC, 'media', ep)
        os.makedirs(media_dir, exist_ok=True)

        count = 0
        with zipfile.ZipFile(f) as z:
            for name in z.namelist():
                if name.startswith('word/media/') and not name.endswith('/'):
                    dest = os.path.join(media_dir, os.path.basename(name))
                    with z.open(name) as src_f, open(dest, 'wb') as dst_f:
                        shutil.copyfileobj(src_f, dst_f)
                    count += 1
        total_extracted += count
        if count > 0:
            print(f"  Episode {ep}: extracted {count} images")

    print(f"  -> Total extracted: {total_extracted} images")

    # ── Step 3: Fix image paths in markdown ──
    # Pandoc may emit:
    #   (a) Absolute paths with doubled media: E:\...\media\08/media/image1.jpeg
    #   (b) Flat paths without episode: media/image1.jpeg
    # Handle both cases.
    print("\n=== Step 3: Fix image paths in markdown ===")
    bad_prefix = SRC + '\\media\\'
    files_fixed = 0

    for md_file in md_files:
        with open(md_file, encoding='utf-8') as f:
            content = f.read()

        # (a) Strip absolute prefix and fix doubled media/ layer
        if bad_prefix in content:
            content = content.replace(bad_prefix, 'media/')
            content = re.sub(r'(media/\d+/)media/', r'\1', content)

        # (b) Inject episode number into flat media/image paths
        ep_match = re.match(r'(\d+)', os.path.basename(md_file))
        if ep_match:
            ep = ep_match.group(1)
            # Replace media/imageN.ext -> media/<ep>/imageN.ext (only if not already <ep>/)
            content = re.sub(
                r'media/(?!(?:\d+/))(\w+\.\w+)',
                rf'media/{ep}/\g<1>',
                content
            )

        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)
        files_fixed += 1

    if files_fixed > 0:
        print(f"  Fixed paths in {files_fixed} files")
    else:
        print("  No path fixes needed")

    # Clean up stale media/<ep>/media files/dirs
    print("\n=== Cleanup: removing stale nested media/ ===")
    for root, dirs, files in os.walk(os.path.join(SRC, 'media')):
        for d in dirs:
            if d == 'media':
                stale_dir = os.path.join(root, d)
                shutil.rmtree(stale_dir, ignore_errors=True)
                print(f"  Removed stale dir: {stale_dir}")
        for fn in files:
            if '/media/' in os.path.join(root, fn).replace(SRC, ''):
                stale_file = os.path.join(root, fn)
                try:
                    os.remove(stale_file)
                    print(f"  Removed stale file: {stale_file}")
                except OSError:
                    pass

    # ── Post-conversion checklist ──
    print("\n" + "=" * 60)
    print("POST-CONVERSION CHECKLIST")
    print("=" * 60)

    failed = []

    # 1. .md file count equals original .docx count
    md_count = len(md_files)
    docx_count = len(docx_files)
    if md_count == docx_count:
        print(f"\n[1] .md count ({md_count}) == .docx count ({docx_count}): PASS")
    else:
        print(f"\n[1] .md count ({md_count}) == .docx count ({docx_count}): FAIL")
        failed.append("md_count_mismatch")

    # 2. Every <img src="..."> uses relative path starting with media/
    img_issues = []
    for md_file in md_files:
        with open(md_file, encoding='utf-8') as f:
            content = f.read()
        for m in re.finditer(r'<img\s+src="([^"]+)"', content):
            src = m.group(1)
            if not src.startswith('media/'):
                img_issues.append((os.path.basename(md_file), src))
    if not img_issues:
        print(f"[2] All img src start with 'media/': PASS")
    else:
        print(f"[2] All img src start with 'media/': FAIL")
        for f, s in img_issues[:5]:
            print(f"    BAD: {f} -> {s}")
        failed.append("bad_img_prefix")

    # 3. Every referenced image exists
    missing = []
    for md_file in md_files:
        with open(md_file, encoding='utf-8') as f:
            content = f.read()
        for m in re.finditer(r'<img\s+src="([^"]+)"', content):
            src = m.group(1)
            img_path = os.path.join(SRC, src)
            if not os.path.exists(img_path):
                missing.append((os.path.basename(md_file), src))
    if not missing:
        print(f"[3] All referenced images exist: PASS")
    else:
        print(f"[3] All referenced images exist: FAIL")
        for f, s in missing[:10]:
            print(f"    MISSING: {f} -> {s}")
        failed.append("missing_images")

    # 4. No zero-byte images
    all_images = []
    for root, dirs, files in os.walk(os.path.join(SRC, 'media')):
        for fn in files:
            all_images.append(os.path.join(root, fn))
    zero = [i for i in all_images if os.path.getsize(i) == 0]
    if not zero:
        print(f"[4] No zero-byte images: PASS")
    else:
        print(f"[4] No zero-byte images: FAIL ({len(zero)} zero-byte files)")
        for z in zero[:5]:
            print(f"    ZERO: {z}")
        failed.append("zero_byte_images")

    # 5. No stale media/<ep>/media files or dirs
    stale = []
    for root, dirs, files in os.walk(os.path.join(SRC, 'media')):
        for fn in files:
            rel_path = os.path.join(root, fn).replace(SRC, '')
            if '/media/' in rel_path:
                stale.append(os.path.join(root, fn))
    if not stale:
        print(f"[5] No stale media/<ep>/media files: PASS")
    else:
        print(f"[5] No stale media/<ep>/media files: FAIL")
        for s in stale[:5]:
            print(f"    STALE: {s}")
        failed.append("stale_nested_media")

    print()
    print("=" * 60)
    if not failed:
        print("ALL CHECKS PASSED")
    else:
        print(f"SOME CHECKS FAILED: {', '.join(failed)}")
    print("=" * 60)


if __name__ == '__main__':
    main()
