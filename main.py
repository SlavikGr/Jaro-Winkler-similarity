from pyjarowinkler import distance

# дані, які повинні бути
name_work = '' # список назви робіт
abstract_work = '' # список абстрактів робіт
keywords = '' # ключові слова діяльності

# Порівняння слів абстракту з ключовими словами діяльності за допомогою Джаро-Вінклера
    def metrics(self, abstract_work, keywords):
        avrg_values_abstract = []
        abstract_is_none = False
        ind = 0
        for work in abstract_work:
            if work:
                word = work.split(' ')
                max_value_word = []
                for w in word:
                    if len(w) > 3:
                        result_word = self.similar_word_with_key(w, keywords)
                        max_value_word.append(result_word)
                result_abstract = self.average_value_one_work(max_value_word, 10)
                avrg_values_abstract.append(result_abstract)
            else:
                abstract_is_none = True
                print('abstract_is_none', abstract_is_none)

            if abstract_is_none:
                avrg_values_name_work = self.score_by_name_work(name_work[ind], keywords)
                print("avrg_values_name_work", avrg_values_name_work)
                avrg_values_abstract.extend(avrg_values_name_work)
            ind += 1

        print('RESULT ', avrg_values_abstract)
        avrg_values_all_work = (sum(avrg_values_abstract) / len(avrg_values_abstract)) * 100
        print("Average:", avrg_values_all_work)
        return float("{0:.2f}".format(avrg_values_all_work))


    # Порівняння ключових слів зі словом з абстракту, повернення максимального числа схожості
    def similar_word_with_key(self, w, keywords):
        word_key = []
        for key in keywords:
            word_key.append(distance.get_jaro_distance(w, key, winkler=True, scaling=0.1))
        return max(word_key)

    # Показник схожості науковця і однієї його роботи
    def average_value_one_work(self, max_value_word, n):
        max_value_word.sort()
        max_values_in_name_work = max_value_word[-n:]
        # Середнє значення 10 найбільших показників
        avrg = (sum(max_values_in_name_work) / n)
        return avrg


    # Якщо робота не має абстракту, то аналіз проводиться по назві роботи
    def score_by_name_work(self, name_work, keywords):
        avrg_values_name_work = []
        for work in name_work:
            if work:
                word = work[0].split(' ')
                max_value_word = []
                for w in word:
                    if len(w) > 3:
                        result_word = self.similar_word_with_key(w, keywords)
                        max_value_word.append(result_word)
                result_name_work = self.average_value_one_work(max_value_word, 3)
                avrg_values_name_work.append(result_name_work)
        return avrg_values_name_work
