v = input()
st = []
for each_brac in v:
    if(each bracket == '[' or '{' or '('): 
        st.append(each_brac)

else:
    top = st[-1]
    if(top == '(' and each bracket == ')'):
        st.pop()

        print("Balanced")

    else:
        print("Unbalanced")    
        
    
