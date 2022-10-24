# arg and kwarg
# 1. *arg 함수 정의할떄 사용
# 가변 갯수의 인자들을 함수에 넣어줌
# 가변 갯수 : 갯수가 변할 수 있는 상황에서 사용 가능
def test_var_args(f_arg,*argv):
    print('첫번째 인자:',f_arg)
    for arg in argv:
        print("*arg의 다른 인자",arg)
test_var_args('야숩','python','달걀','test')
