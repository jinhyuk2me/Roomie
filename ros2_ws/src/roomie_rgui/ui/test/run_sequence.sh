#!/bin/bash

echo "🏠 Roomie UI 시퀀스 실행 스크립트"
echo "=================================="

# 현재 디렉토리 확인
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "📂 실행 디렉토리: $SCRIPT_DIR"

# Python 가상환경 체크
if [[ -n "$VIRTUAL_ENV" ]]; then
    echo "✅ Python 가상환경 활성화됨: $VIRTUAL_ENV"
else
    echo "⚠️  Python 가상환경이 활성화되지 않았습니다."
    echo "💡 다음 명령으로 가상환경을 활성화하세요:"
    echo "   source /home/jinhyuk2me/venv/opencv_venv/bin/activate"
fi

echo ""
echo "🚀 Roomie UI 시퀀스를 시작합니다..."
echo "💡 전체화면으로 실행됩니다. ESC 키로 종료할 수 있습니다."
echo ""

# Python 스크립트 실행
cd "$SCRIPT_DIR"
python roomie_ui_sequence.py

echo ""
echo "👋 Roomie UI 시퀀스가 종료되었습니다." 