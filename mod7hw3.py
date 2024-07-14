class WordsFinder:
    def __init__(self, *file_names: tuple):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        symbol_del = [',', '.', '=', '!', '?', ';', ':', ' - ']
        words = []
        for file_name in self.file_names:
            with open(file_name , encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for symbol in symbol_del:
                        if line.count(symbol):
                            line = line.replace(symbol, "")
                    line = line.split()
                    words.extend(line)
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            if word in words:
                result[file_name] = words.index(word) + 1
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word)
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
