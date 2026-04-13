# def outer():
#     print("Inside outer")
#     def inner():
#         print("Inside inner")
#     return inner
# res=outer()
# print(res)
# res()
def outer():
    print("Inside Outer")
    def inner():
        print("Inside inner")
    inner()
outer()