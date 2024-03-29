<h1>goit-algo-hw-06</h1>


<h2>Завдання 1:</h2>

Створено граф, який моделює реальну мережу, з ***15 вузлами та 19 ребрами.***
***Густина графа становить 0.09048, що свідчить про те, що він є досить розрідженим.***

<h2>Завдання 2: Порівняння DFS і BFS алгоритмів</h2>

**DFS (Depth-First Search) та BFS (Breadth-First Search)** - це два основних алгоритми для пошуку шляхів у графах.

**DFS** характеризується тим, що він досліджує граф до глибини, перед тим як вивести результат. Це означає, що він спрямований на об'єкти (вершини), які знаходяться глибше в структурі графа, перед тим як вивести ті, що на поверхні. Таким чином, результат DFS може бути не найближчим шляхом від однієї вершини до іншої, а просто одним з можливих шляхів.

Навпаки, **BFS** розглядає всі можливі шляхи на одному рівні від початкової вершини перед переходом до вершин на наступному рівні. Це означає, що результат **BFS** завжди буде найкоротшим шляхом від однієї вершини до іншої в ненапрямленому графі без ваг.

У вашому випадку результати обох алгоритмів однакові, оскільки немає перешкод на шляху і найкоротший шлях знаходиться на одному рівні.

<h2>Завдання 3: Алгоритм Дейкстри</h2>

**Алгоритм Дейкстри - це алгоритм пошуку найкоротшого шляху в графі з не від'ємними вагами ребер. Він працює дуже добре для таких ситуацій, оскільки завжди знаходить найкоротший шлях від однієї вершини до всіх інших.**

У вашому випадку, коли були додані ваги ребер, алгоритм Дейкстри знайшов найкоротший шлях від "Shopping Mall" до кожної іншої вершини в графі. Це дозволяє з легкістю визначити найкоротший шлях від однієї точки до іншої, враховуючи ваги ребер.

**В цілому, результати алгоритмів DFS, BFS та Дейкстри показують їхню ефективність у вирішенні різних завдань у графах, залежно від умов задачі.**
