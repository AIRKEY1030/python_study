# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = sentence.split()
result = {}
num_first = [1, 5, 6, 7, 8, 9, 15, 16, 19]

for (num, word) in enumerate(words, 1):
    if num in num_first:
        result[word[0:1]] = num
    else:
        result[word[0:2]] = num

print(result)


# %%
# emurate リストの順番をディクショナリに渡す
