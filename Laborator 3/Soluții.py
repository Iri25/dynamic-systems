#!/usr/bin/env python
# coding: utf-8

# In[5]:


# exercice 1
# a
t = var('t')
x = function('x')(t)
y = function('y')(t)
deq1 = diff(x, t) == x + 4*y
deq2 = diff(y, t) == x + y
syst = [deq1, deq2]

desolve_system(syst, [x, y])
sol_syst = desolve_system(syst, [x, y])

show(sol_syst)


# In[6]:


# exercice 1
# b
t = var('t')
x = function('x')(t)
y = function('y')(t)
deq1 = diff(x, t) == 2*x - y
deq2 = diff(y, t) == x + 2*y
syst = [deq1, deq2]

desolve_system(syst, [x, y])
sol_syst = desolve_system(syst, [x, y])

show(sol_syst)


# In[7]:


# exercice 1
# c
t = var('t')
x = function('x')(t)
y = function('y')(t)
z = function('z')(t)
deq1 = diff(x, t) == x - y + z
deq2 = diff(y, t) == x + y - z
deq3 = diff(y, t) == -y + 2*z
syst = [deq1, deq2, deq3]

desolve_system(syst, [x, y, z])
sol_syst = desolve_system(syst, [x, y, z])

show(sol_syst)


# In[88]:


# exercice 1
# d
t = var('t')
x = function('x')(t)
y = function('y')(t)
deq1 = diff(x, t) == 5*x + 3*y + 1
deq2 = diff(y, t) == -6*x - 4*y + exp(-t)
syst = [deq1, deq2]

desolve_system(syst, [x, y])
sol_syst = desolve_system(syst, [x, y])

show(sol_syst)


# In[89]:


# exercice 1
# e
t = var('t')
x = function('x')(t)
y = function('y')(t)
deq1 = diff(x, t) == x + 3*y + cos(t)
deq2 = diff(y, t) == x - y + 2*t
syst = [deq1, deq2]

desolve_system(syst, [x, y])
sol_syst = desolve_system(syst, [x, y])

show(sol_syst)


# In[90]:


# exercice 1
# f
t = var('t')
x = function('x')(t)
y = function('y')(t)
z = function('z')(t)
deq1 = diff(x, t) == x - 2*y - 2*z + exp(-t)
deq2 = diff(y, t) == -2*x + y + 2*z
deq3 = diff(z, t) == 2*x - y - 3*z + exp(-t)
syst = [deq1, deq2, deq3]

desolve_system(syst, [x, y, z])
sol_syst = desolve_system(syst, [x, y, z])

show(sol_syst)


# In[18]:


# exercice 2
# a
t = var('t')
x = function('x')(t)
y = function('y')(t)
deq1 = diff(x, t) == x + 4*y
deq2 = diff(y, t) == x + y
syst = [deq1, deq2]

vars = [x, y]
in_cond = [0, 1, 2]

sol = desolve_system(syst, vars, in_cond)

sol_x(t) = sol[0].rhs()
sol_y(t) = sol[1].rhs()

g1 = plot(sol_x(t), t, -6, 6, color = 'red')
g2 = plot(sol_y(t), t, -6, 6, color = 'blue')

show(g1 + g2)


# In[23]:


# exercice 2
# b
t = var('t')
x = function('x')(t)
y = function('y')(t)
deq1 = diff(x, t) == x - y + t - 1
deq2 = diff(y, t) == -2*x + 4*y + cos(t)
syst = [deq1, deq2]

vars = [x, y]
in_cond = [0, 0, 1]

sol = desolve_system(syst, vars, in_cond)

sol_x(t) = sol[0].rhs()
sol_y(t) = sol[1].rhs()

g1 = plot(sol_x(t), t, -4, 8, color = 'red')
g2 = plot(sol_y(t), t, -4, 8, color = 'blue')

show(g1 + g2)


# In[25]:


# exercice 2
# c
t = var('t')
x = function('x')(t)
y = function('y')(t)
deq1 = diff(x, t) == x + 2*y + exp(-t)
deq2 = diff(y, t) == -2*x + y + 1
syst = [deq1, deq2]

vars = [x, y]
in_cond = [0, 0, 1]

sol = desolve_system(syst, vars, in_cond)

sol_x(t) = sol[0].rhs()
sol_y(t) = sol[1].rhs()

g1 = plot(sol_x(t), t, -4, 6, color = 'red')
g2 = plot(sol_y(t), t, -4, 6, color = 'blue')

show(g1 + g2)


# In[92]:


# exercice 2
# d
t = var('t')
x = function('x')(t)
y = function('y')(t)
z = function('z')(t)
deq1 = diff(x, t) == -x + 3*y + 3*z + 27*t^2
deq2 = diff(y, t) == 2*x - 2*y - 5*z + 3*t
deq3 = diff(z, t) == -2*x + 3*y + 6*z + 3
syst = [deq1, deq2, deq3]

vars = [x, y, z]
in_cond = [0, 50, -30, 26]

sol = desolve_system(syst, vars, in_cond)

sol_x(t) = sol[0].rhs()
sol_y(t) = sol[1].rhs()

g1 = plot(sol_x(t), t, -4, 6, color = 'red')
g2 = plot(sol_y(t), t, -4, 6, color = 'blue')

show(g1 + g2)


# In[28]:


# exercice 3
# a
t = var('t')
x = function('x')(t)
y = function('y')(t)
deq1 = diff(x, t) == x + y
deq2 = diff(y, t) == -2*x + 4*y 
syst = [deq1, deq2]

vars = [x, y]
in_cond = [0, 3, 0]
#in_cond = [0, 0, 3]
#in_cond = [0, -3, 0]
#in_cond = [0, 0, -3]
sol = desolve_system(syst, vars, in_cond)

sol_x(t) = sol[0].rhs()
sol_y(t) = sol[1].rhs()

show(sol_x)
show(sol_y)


# In[35]:


# exercice 3
# b
t = var('t')
x = function('x')(t)
y = function('y')(t)
deq1 = diff(x, t) == x + y
deq2 = diff(y, t) == -2*x + 4*y 
syst = [deq1, deq2]

vars = [x, y]
#in_cond = [0, 3, 0]
in_cond = [0, 0, 3]
#in_cond = [0, -3, 0]
#in_cond = [0, 0, -3]
sol = desolve_system(syst, vars, in_cond)

sol_x(t) = sol[0].rhs()
sol_y(t) = sol[1].rhs()

limit_x = limit(sol_x(t), t=infinity)
limit_y = limit(sol_y(t), t=infinity)

show(limit_x)
show(limit_y)


# In[66]:


# exercice 3
# c
reset()
t = var('t')
x = function('x')(t)
y = function('y')(t)
deq1 = diff(x, t) == x + y
deq2 = diff(y, t) == -2*x + 4*y 
syst = [deq1, deq2]

vars = [x, y]
in_cond = [0, 3, 0]
#in_cond = [0, 0, 3]
#in_cond = [0, -3, 0]
#in_cond = [0, 0, -3]
sol = desolve_system(syst, vars, in_cond)

sol_x(t) = sol[0].rhs()
sol_y(t) = sol[1].rhs()

g1 = plot(sol_x(t), t, -4, 4, color = 'red', ymin = -20)
g2 = plot(sol_y(t), t, -4, 4, color = 'blue', ymax = 20)

show(g1 + g2)

f1(u,v) = u + v
f2(u,v) = -2*u + 4*v

h1 = plot_vector_field([f1(u,v), f2(u,v)], [u, -10, 10], [v, -10, 10], color = 'red')
h2 = parametric_plot((sol_x(t), sol_y(t)), (t, -10, 10), color = 'blue')
h = h1 + h2

h.show(xmin = -5, xmax = 5, ymin = -5, ymax = 5)


# In[44]:


# exercice 4
# a
t = var('t')
x = function('x')(t)
y = function('y')(t)
deq1 = diff(x, t) == y
deq2 = diff(y, t) == -x - 2*y
syst = [deq1, deq2]

desolve_system(syst, [x, y])
sol_syst = desolve_system(syst, [x, y])

show(sol_syst)


# In[49]:


# exercice 4
# b
t = var('t')
x = function('x')(t)
y = function('y')(t)
deq1 = diff(x, t) == y
deq2 = diff(y, t) == -x - 2*y

desolve_system(syst, [x, y])
sol_syst = desolve_system(syst, [x, y])

sol_x(t) = sol_syst[0].rhs()
sol_y(t) = sol_syst[1].rhs()

limit_x = limit(sol_x(t), t=infinity)
limit_y = limit(sol_y(t), t=infinity)

show(limit_x)
show(limit_y)


# In[73]:


# exercice 4
# c
reset()
t = var('t')
x = function('x')(t)
y = function('y')(t)
deq1 = diff(x, t) == y
deq2 = diff(y, t) == -x - 2*y
syst = [deq1, deq2]

sol = desolve_system(syst, [x,y], [0, 0, 3])

sol_x(t) = sol[0].rhs()
sol_y(t) = sol[1].rhs()

f1(u,v) = u + v
f2(u,v) = -2*u + 4*u
n = sqrt(f1(u,v)^2 + f2(u,v)^2)

h1 = plot_vector_field([f1(u,v), f2(u,v)], [u, -10, 10], [v, -10, 10], color = 'red', aspect_ratio = 1)
h2 = parametric_plot((sol_x(t), sol_y(t)), (t, -10, 10), color = 'blue')
h = h1 + h2

h.show(xmin = -5, xmax = 5, ymin = -5, ymax = 5)


# In[81]:


# exercice 5
# a

f1(u, v) = 2*u + v
f2(u, v) = u + 2*u
n = sqrt(f1(u, v)^2 + f2(u, v)^2)

g = plot_vector_field([f1(u, v), f2(u, v)], [u, -10, 10], [v, -10, 10], color = 'red', aspect_ratio = 1)

show(g)


# In[82]:


# exercice 5
# b

f1(u, v) = -u - v
f2(u, v) = u - v
n = sqrt(f1(u, v)^2 + f2(u, v)^2)

g = plot_vector_field([f1(u, v), f2(u, v)], [u, -10, 10], [v, -10, 10], color = 'red', aspect_ratio = 1)

show(g)


# In[83]:


# exercice 5
# c

f1(u, v) = v
f2(u, v) = -u 
n = sqrt(f1(u, v)^2 + f2(u, v)^2)

g = plot_vector_field([f1(u, v), f2(u, v)], [u, -10, 10], [v, -10, 10], color = 'red', aspect_ratio = 1)

show(g)


# In[85]:


# exercice 5
# d

f1(u, v) = -2*u
f2(u, v) = -4*u - 2*v
n = sqrt(f1(u, v)^2 + f2(u, v)^2)

g = plot_vector_field([f1(u, v), f2(u, v)], [u, -10, 10], [v, -10, 10], color = 'red', aspect_ratio = 1)

show(g)


# In[86]:


# exercice 5
# e

f1(u, v) = u - 4*v
f2(u, v) = 5*u - 3*v
n = sqrt(f1(u, v)^2 + f2(u, v)^2)

g = plot_vector_field([f1(u, v), f2(u, v)], [u, -10, 10], [v, -10, 10], color = 'red', aspect_ratio = 1)

show(g)


# In[87]:


# exercice 5
# f

f1(u, v) = 3*u - v
f2(u, v) = v
n = sqrt(f1(u, v)^2 + f2(u, v)^2)

g = plot_vector_field([f1(u, v), f2(u, v)], [u, -10, 10], [v, -10, 10], color = 'red', aspect_ratio = 1)

show(g)


# In[ ]:




