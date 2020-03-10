
# coding: utf-8

# # Programa para validar e-mail

# In[3]:


#Programa para validar e-mail
nome = str(input("Digite o nome do funcionario(a): "))
email = str(input("Digite o email do funcionario(a): "))
def valid_email(string):
    pos = string.find("@")
    dot = string.rfind(".")
    if pos < 1:
        return False
    if dot < pos + 2:
        return False
    if dot + 2 >= len(string):
        return False
    return True
print("E-mail aprovado do funcionario(a) ! ")
        

