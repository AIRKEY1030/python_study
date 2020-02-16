# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
word1 = 'パトカー'
word2 = 'タクシー'
result = ''

for (a, b) in zip(word1, word2):
    result += a + b

print(result)


# %%
# zip 複数のリストから要素を集めたリストを作る
target1 = 'abcde'
target2 = '12345'
res_zip = zip(target1, target2)
list(res_zip)
[('a', '1'), ('b', '2'), ('c', '3'), ('d', '4'), ('e', '5')]


# %%
