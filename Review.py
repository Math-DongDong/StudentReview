import streamlit as st
import streamlit.components.v1 as components

# 페이지 설정: 전체 너비 레이아웃과 제목 설정
st.set_page_config(layout="wide", page_title="학생 소감문 관리 시스템")

# Google Apps Script 링크
url = "https://script.google.com/macros/s/AKfycby5nDFCp5VnX8c9aACff91NcZ28atWXriTfixlSBGb5hkE7J2ZOAOBscf494LNagrkw/exec"

# iframe을 사용하여 URL을 Streamlit 화면 내에서 렌더링
components.html(f'<iframe src="{url}" width="100%" height="600" frameborder="0"></iframe>', height=600)