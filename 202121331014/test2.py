import jieba
from collections import Counter
import time


def get_similarity_score(original_text, plagiarized_text):
    try:
        # 分词
        original_words = list(jieba.cut(original_text))
        plagiarized_words = list(jieba.cut(plagiarized_text))

        # 构建词频统计
        original_word_count = Counter(original_words)
        plagiarized_word_count = Counter(plagiarized_words)

        # 计算余弦相似度
        intersection = set(original_word_count.keys()) & set(plagiarized_word_count.keys())
        numerator = sum([original_word_count[word] * plagiarized_word_count[word] for word in intersection])
        denominator = (sum([original_word_count[word] ** 2 for word in original_word_count.keys()]) ** 0.5) * (
                sum([plagiarized_word_count[word] ** 2 for word in plagiarized_word_count.keys()]) ** 0.5)

        if denominator == 0:
            similarity_score = 0
        else:
            similarity_score = numerator / denominator

        return similarity_score * 100

    except Exception as e:
        raise Exception("计算相似度时发生错误：" + str(e))


def main():
    try:
        # 获取原文文件路径
        original_file_path = "orig.txt"

        # 获取抄袭版论文文件路径
        plagiarized_file_path = "orig_add.txt"

        # 获取答案文件路径
        answer_file_path = "D:\PyCharm 2022.3.1\Python\out.txt"

        # 读取原文文件和抄袭版论文文件的内容
        start_time = time.time()  # 开始计时
        with open(original_file_path, 'r', encoding='utf-8') as original_file:
            original_text = original_file.read()
        with open(plagiarized_file_path, 'r', encoding='utf-8') as plagiarized_file:
            plagiarized_text = plagiarized_file.read()
        end_time = time.time()  # 结束计时
        read_time = end_time - start_time  # 文件读取耗时

        # 计算重复率
        start_time = time.time()  # 开始计时
        similarity_score = get_similarity_score(original_text, plagiarized_text)
        end_time = time.time()  # 结束计时
        similarity_time = end_time - start_time  # 相似度计算耗时

        # 将重复率写入答案文件
        with open(answer_file_path, 'w', encoding='utf-8') as answer_file:
            answer_file.write(f"重复率: {similarity_score:.2f}%\n")
        print(f"重复率: {similarity_score:.2f}%")
        print(f"文件读取耗时: {read_time:.2f}秒")
        print(f"相似度计算耗时: {similarity_time:.2f}秒")

    except Exception as e:
        raise Exception("执行过程中发生错误：" + str(e))


try:
    main()
except Exception as e:
    print("发生错误：" + str(e))
