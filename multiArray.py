# coding: utf-8
# Your code here!

#list0 = []
list1 = [
        ["SHINAGAWA","TAMACHI"],
        ["OOIMACHI","OOMORI","KAMATA"],
        ["SHIBUYA","IKEBUKURO","TAKADANOBABA","YOYOGI"]
        ]

#print(len(list1))

#len(list1):���s���邩 3
#len(list1[0]):�ォ��0�Ԗڂ̔z��̒��� 2
#�����g�ݍ��킹��ƁB�B�B

for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j]),
    print("\n")
    
#i��len(list1)�J��Ԃ� �� i��3��J��Ԃ�
#�J��Ԃ�����j��len(list1[i])�J��Ԃ� �� j��list1[i]��J��Ԃ� �� i��0�̂Ƃ���0�Ԗڂ̔z��̒����J��Ԃ� �� 2��J��Ԃ�
#�܂�A������������
#i��0�̂Ƃ�j�͏ォ��0�Ԗڂ̒�����j�����[�v������A0�̂Ƃ�2��J��Ԃ�
#i:0 j:2, i:1 j:3, i:2 j:4
