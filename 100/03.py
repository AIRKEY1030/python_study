# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
result = list()

words = sentence.split(' ')

for word in words:
    count = 0
    for char in word:
        # print(char)
        if char.isalpha():
            count += 1
    result.append(count)

print(result)


# %%
#　データの集まりに単語を指定すると1文字ずつ数える
