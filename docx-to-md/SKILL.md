---
name: docx-to-md
description: Convert 通义听悟 docx transcripts or any batch of .docx files to markdown with images. Use when the user mentions docx转md, docx to markdown, 通义听悟转录文件转换, 批量docx, or needs .docx files converted to .md.
---

# Docx to Markdown

Three-step pipeline: pandoc for text, Python zipfile for images, regex for path fixup. Each step completes before the next begins.

**Unified script:** `convert_all.py` — run it directly from the source directory:
```
python convert_all.py <source-directory>
```
If no directory is given, uses the current working directory.
The script runs all three steps plus the full verification checklist.

## Non-Negotiable Rules

- **Pandoc handles text only.** Do not trust `--extract-media` on Windows — it under-extracts images (10 embedded images → 1 stale file). Extract images manually from the docx zip.
- **One media subdirectory per episode.** Every docx uses `image1.jpeg`, `image2.jpeg` — colliding into one `media/` dir overwrites. Pattern: `media/<ep-number>/`.
- **Never touch Chinese paths from bash.** Python `os.walk`/`glob` survive encoding wobble; `ls`/`cp` in bash do not. Run conversions through Python scripts, not shell one-liners.
- **Fix img paths after conversion.** Pandoc emits paths in different formats depending on version/platform — either absolute with doubled `media/` (`E:\...\media\08/media/image1.jpeg`) or flat without episode number (`media/image1.jpeg`). The script handles both.
- **Docx source files are not deleted.** Leave them until the user confirms.
- **Avoid Unicode checkmarks in terminal output.** Windows GBK terminals choke on `✓`/`✗`. Use plain `PASS`/`FAIL` strings.
- **GBK-proof all print statements.** Filenames may contain Unicode chars outside GBK range (e.g. ``). `print()` on a GBK terminal will crash with `UnicodeEncodeError`. Use encode/decode guards:
  ```python
  def safe_print(*args, **kwargs):
      text = ' '.join(str(a) for a in args)
      try:
          print(text, **kwargs)
      except UnicodeEncodeError:
          print(text.encode('gbk', errors='replace').decode('gbk'), **kwargs)

  def safe_name(path):
      name = os.path.basename(path)
      try:
          name.encode('gbk')
          return name
      except UnicodeEncodeError:
          return name.encode('gbk', errors='replace').decode('gbk')
  ```

## Step 1 — Pandoc text conversion

Convert every `.docx` in the source directory to `.md` using pandoc with `gfm` output and `--wrap=none`.

**Completion criterion:** `.md` count equals `.docx` count in the directory.

```python
import subprocess, os, glob

src = r'<source-directory>'
pandoc = r'C:\Users\ASUS\AppData\Local\Pandoc\pandoc'

for f in sorted(glob.glob(os.path.join(src, '*_原文.docx'))):
    out_md = f.replace('_原文.docx', '.md')
    safe_print(f"  Converting: {safe_name(f)}")
    subprocess.run([
        pandoc, f, '-f', 'docx', '-t', 'gfm', '--wrap=none', '-o', out_md
    ])
```

## Step 2 — Extract images from docx zip

Open each docx as a zipfile. Pull every `word/media/*` entry into `media/<ep>/`, where `<ep>` is the episode number parsed from the filename prefix.

**Completion criterion:** image count across all `media/` subdirs matches the sum of `word/media/*` entries across all docx files.

```python
import zipfile, shutil, os, re

for f in glob.glob(os.path.join(src, '*_原文.docx')):
    ep = re.match(r'(\d+)', os.path.basename(f)).group(1)
    media_dir = os.path.join(src, 'media', ep)
    os.makedirs(media_dir, exist_ok=True)

    with zipfile.ZipFile(f) as z:
        for name in z.namelist():
            if name.startswith('word/media/') and not name.endswith('/'):
                dest = os.path.join(media_dir, os.path.basename(name))
                with z.open(name) as src_f, open(dest, 'wb') as dst_f:
                    shutil.copyfileobj(src_f, dst_f)
```

## Step 3 — Fix image paths in markdown

Pandoc can emit image paths in two forms. Handle both per `.md` file:

1. Absolute paths with doubled `media/`: `E:\...\nginx_md\media\08/media/image1.jpeg` → `media/08/image1.jpeg`
2. Flat paths (no episode number): `media/image1.jpeg` → `media/<ep>/image1.jpeg`

Also clean up any stale `media/<ep>/media` file or directory that pandoc may have created.

**Completion criterion:** every `<img src="">` in every `.md` resolves to an existing file when joined with the source directory.

```python
import re, os

bad_prefix = src + '\\media\\'

for md_file in glob.glob(os.path.join(src, '*.md')):
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
        content = re.sub(
            r'media/(?!(?:\d+/))(\w+\.\w+)',
            rf'media/{ep}/\g<1>',
            content
        )

    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(content)
```

## Post-Conversion Checklist

Run after Step 3. Every item must pass before reporting success:

- [ ] `.md` file count equals original `.docx` count
- [ ] Every `<img src="...">` uses a relative path starting with `media/`
- [ ] Every referenced image exists at that relative path from the source directory
- [ ] No zero-byte images in any `media/` subdirectory
- [ ] No stale `media/<ep>/media` files or directories remain

## Why Not Other Tools

- **mammoth**: not pre-installed; pandoc is.
- **python-docx**: reads docx but doesn't convert to markdown.
- **pandoc `--extract-media` alone**: broken on Windows for multi-image docx files — extracts one stub file instead of all embedded images.
- **bash loops over Chinese paths**: encoding instability across shell invocations. Python `os.walk`/`glob` is reliable.
