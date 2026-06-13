import re
import shutil
from pathlib import Path


def on_post_build(config, **_):
    src = Path(config["config_file_path"]).parent / "archive"
    dst = Path(config["site_dir"])
    if not src.is_dir():
        return
    archive_dst = dst / "archiv"
    archive_dst.mkdir(exist_ok=True)
    for item in src.iterdir():
        if item.name == "index.html":
            html = item.read_text(encoding="utf-8")
            html = re.sub(
                r"<head(\s[^>]*)?>",
                lambda m: m.group(0) + '\n  <base href="../" />',
                html,
                count=1,
                flags=re.IGNORECASE,
            )
            (archive_dst / "index.html").write_text(html, encoding="utf-8")
            continue
        target = dst / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)
