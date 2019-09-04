import matplotlib.pyplot as plt
from matplotlib import style # importando estilos pré-definidos no matplotlib

style.use('ggplot')

# Brincando com gráficos de linha
X = range(100)
Y = [value ** 2 for value in X]
Z = [value ** 3 for value in X]
plt.plot(X, Y, label='n^2')
plt.plot(X, Z, '--', label='n^3')
plt.plot(Y, X, label='n')
plt.title('Curvas exponenciais')
plt.xlabel('Valores de n')
plt.ylabel('Valores de n² e n³')
plt.legend()
plt.grid(True)
plt.show()

# Gráficos de barra
people = ['Julio', 'Diarley', 'Gabriel']
scores = [29, 72, 102]
plt.bar(people, scores)
plt.barh(people, scores)
plt.show()

# Gráficos de pizza
labels = ['lasanha', 'cerveja', 'cannabis']
data = [13, 45, 80]
plt.pie(data, labels=labels)

# Histogramas
data = [13, 13, 13, 45, 80, 80, 80, 80, 80, 80]
plt.hist(data)
plt.show()
