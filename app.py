# 스프림릿 라이브러리를 사용하기 위한 임포트문 작성

# 스트림릿 라이브러리는 이미 설치했다!!
# pip install streamlit

# 위의 라이브러리는 설치했으므로, 임포트만 하면 된다.
import streamlit as st

# 웹 대시보드 개발 라이브러리 스트림릿은 
# main 함수가 있어야 한다.

def main() :
    st.title('Hello Streamlit. 웹 대시보드')
    st.text('웹 대시보드 개발하기')

    name = '홍길동'


    st.text('제 이름은 {}입니다.'.format(name))

    st.header('이 영역은 헤더 영역')
    st.subheader('이 영역은 subheader 영역')

    st.success('성공했을때의 메시지 영역')
    st.warning('이 영역은 경고 영역')
    st.info('정보를 보여주고 싶을떄')
    st.error('문제가 발생했음을 알려주고 싶을때')

    st.help(range)
    st.help(sum)

if __name__ == '__main__' :
    main()

