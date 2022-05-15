# Kakan

![logo](https://github.com/Kakanom/task/blob/main/Kakan.ico)

---

**В данном проекте представлены модули для:**
 
1. Работы с математикой
2. Предобработки данных
3. Моделей машинного обучения
4. Визуализации

Примеры работы программы:

   Линейная регрессия
    
   ```python
   x = np.array([np.arange(0.0, 6.0, 0.5)]).T
   y = np.array([ 7.32808219,  8.88210587,  8.92239811, 10.52462399, 12.91597313,
           12.55843474, 14.81755614, 18.31825374, 19.44109095, 18.76040251,
           20.07294082, 22.10215284])
    
   mod = LinReg()
   mod.fit(x, y)
    
   draw_lin(x, y, mod.w)
    
   plt.show()
   ```
   ![example_Linear_Regression](https://github.com/Kakanom/task/blob/main/example_Linear_Regression.png)

   Классификация методом Kmeans
   
   ```python
   X, labs = make_blobs(1000, centers = 3)

   mod = Kmeans(n_clusters=3)
   lab = mod.clusterize(X)
    
   draw_poly_class(X, lab)
   plt.show()
   ```
   ![example_Kmeans](https://github.com/Kakanom/task/blob/main/example_Kmeans.png)
   
   

Проект, скорее, будет полезен тем, кто только начинает знакомиться с машинным обучением,
т.к. здесь нет каких-то сложных реализаций, нейронных сетей **(пока что)**.

Конечно, существуют и другие библиотеки для машинного обучения,
но это, все-таки, что-то свое, что я хотел бы развивать.

Для установки библиотеки можно использовать
    ```python
        pip install https://github.com/Kakanom/task.git
    ```

Все нужные для работы проекта библиотеки лежат в файле [requirements](https://github.com/Kakanom/task.git/requirements).

**Good luck**
