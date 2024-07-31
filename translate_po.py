import os
from googletrans import Translator
from polib import pofile
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def translate_po_file(filepath, target_lang):
    translator = Translator()
    po = pofile(filepath)

    for entry in po:
        if not entry.msgstr:  # Only translate if there is no existing translation
            try:
                translation = translator.translate(entry.msgid, dest=target_lang).text
                entry.msgstr = translation
                logger.info(f"Translated '{entry.msgid}' to '{entry.msgstr}'")
            except Exception as e:
                logger.error(f"Error translating '{entry.msgid}': {e}")

    po.save(filepath)

def main():
    locales_dir = 'locale'  # Change this to your locales directory
    target_languages = ['fr', 'ru']  # Both French and Russian

    for target_lang in target_languages:
        for root, dirs, files in os.walk(locales_dir):
            for file in files:
                if file == 'django.po' and target_lang in root:
                    filepath = os.path.join(root, file)
                    logger.info(f'Translating {filepath} to {target_lang}...')
                    translate_po_file(filepath, target_lang)
                    logger.info(f'Translation complete for {filepath}.')

if __name__ == '__main__':
    main()
