# HebEngConv

Hebrew ↔ English conversion tool — command-line and library utilities to convert/normalize Hebrew and English text.

## Quick links
- Repo: https://github.com/nanglister-git/HebEngConv
- Release v1.0.0: https://github.com/nanglister-git/HebEngConv/releases/tag/v1.0.0

## Install
(Example for a Python package — adjust if your project is a different language)

pip install hebengconv

Or run from source:

git clone https://github.com/nanglister-git/HebEngConv.git
cd HebEngConv
python -m pip install -e .

## Usage (example)

# Command-line example
hebengconv --input "akuo" --to he "שלום"

# Library example (Python)
from hebengconv import Converter
c = Converter()
print(c.to_english('יקךךם'))

## Release notes
See RELEASE_NOTES.md or the release page: https://github.com/nanglister-git/HebEngConv/releases/tag/v1.0.0

## Contributing
Contributions welcome. Add a CONTRIBUTING.md and open issues or pull requests. Label "good first issue" for easy starters.

## License
Add a LICENSE file to make this clear (MIT recommended if you want permissive).
