import matplotlib.pyplot as plt

"""
https://www.geeksforgeeks.org/simple-plot-in-python-using-matplotlib/
# x axis values 
x = [1, 2, 3]
# corresponding y axis values 
y = [2, 4, 1]

# plotting the points  
plt.plot(x, y)

# naming the x axis 
plt.xlabel('x - axis')
# naming the y axis 
plt.ylabel('y - axis')

# giving a title to my graph 
plt.title('My first graph!')

# function to show the plot 
plt.show()
"""



def ScoreDoUser(quizz):
    score = 0

    """
    Pergunta_1 -> Qual o animal que a google aluga para o seu uso (cabra)
    Pergunta_2 -> Quando foi inventado o Keyboard do estilo QWERTY (1868)
    Pergunta_3 -> De que material foi feito o primeiro rato (madeira)
    Pergunta_4 -> Qual foi o primeiro tweet da google? (I’m 01100110 01100101 01100101 01101100 01101001 01101110 01100111 00100000 01101100 01110101 01100011 01101011 01111001 00001010)
    """

    if quizz.Q1 == "cabra":
        score += 1

    if quizz.Q2 == "1868":
        score += 1

    if quizz.Q3 == "madeira":
        score += 1

    if quizz.Q4 == "I’m 01100110 01100101 01100101 01101100 01101001 01101110 01100111 00100000 01101100 01110101 01100011 01101011 01111001 00001010":
        score += 1

    return score


def dadosDoQuiz(objects):
    data = {}
    for quizz in objects:
        data[quizz.name] = ScoreDoUser(quizz)
        print(quizz.name)

    return data


def desenha_grafico_resultados(objects):
    data = dadosDoQuiz(objects)
    users = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(users, values, color='white', width=0.5)

    plt.xlabel("users")
    plt.ylabel("score")
    plt.title("Quizz De PW")
    plt.savefig('portfolio/static/portfolio/images/graf.PNG')