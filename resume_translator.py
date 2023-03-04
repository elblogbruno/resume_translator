import argparse
import json
from deep_translator import GoogleTranslator


def translate_text(text, origin_lang, target_lang):
    print("Translating text {0}".format(text))
    translated = GoogleTranslator(source=origin_lang, target=target_lang).translate(text)

    return translated

def parse_rx_resume_json(input_file, output_file, source_lang, target_lang):
    print("Parsing json")

    keys_to_translate = ['headline', 'summary', 'position', 'title', 'level', 'name', 'description']
                         

    with open(input_file) as json_file:
        data = json.load(json_file)

        basics = data['basics']
        basics['headline'] = translate_text(basics['headline'])
        basics['summary'] = translate_text(basics['summary'])

        for p in data['sections'].keys():
            print('Section: ' + p)
            for q in data['sections'][p].keys():
                print('Subsection: ' + q)

                # if data['sections'][p][q] is a STRING translate
                if isinstance(data['sections'][p][q], str) and q in keys_to_translate:
                    data['sections'][p][q] = translate_text(data['sections'][p][q], source_lang, target_lang)
                    continue

                # if data['sections'][p][q] is a INT continue
                if isinstance(data['sections'][p][q], int):
                    continue

                for item in data['sections'][p][q]:
                    for key in keys_to_translate:
                        if key in item:
                            item[key] = translate_text(item[key], source_lang, target_lang)

    if output_file is None:
        output_file = input_file.replace('.json', '_{0}.json'.format(target_lang))

    with open(output_file, 'w') as outfile:
        json.dump(data, outfile)

    return data


def parse_arguments():
    parser = argparse.ArgumentParser(description='Translate resume to other language')
    parser.add_argument('-i', '--input', help='Input file', required=True)
    parser.add_argument('-o', '--output', help='Output file', required=False, default=None)
    parser.add_argument('-s', '--source', help='Source language [EX: es]', required=True, default='es')
    parser.add_argument('-t', '--target', help='Target language [EX: fr]', required=True, default='fr')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    parse_rx_resume_json(args.input, args.output, args.source, args.target)