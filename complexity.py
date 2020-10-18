import math

import plotly.graph_objects as go


length = 100

domain = list(range(1, length + 1))

figure = go.Figure()
figure.add_trace(go.Scatter(x=domain, y=domain, mode='lines+markers', name='O(N)'))
figure.add_trace(go.Scatter(x=domain, y=[x**2 for x in domain], mode='lines+markers', name='O(N^2)'))
figure.add_trace(go.Scatter(x=domain, y=[x**3 for x in domain], mode='lines+markers', name='O(N^3)'))
figure.add_trace(go.Scatter(x=domain, y=[math.log2(x) for x in domain], mode='lines+markers', name='O(log(N))'))
figure.add_trace(go.Scatter(x=domain, y=[x * math.log2(x) for x in domain], mode='lines+markers', name='O(Nlog(N))'))

figure.show()