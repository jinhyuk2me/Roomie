import sys
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLabel, QFrame, QGridLayout, QTableWidgetItem, 
    QProgressBar
)
from PyQt6.QtCore import Qt

STYLESHEET = """
/* 전역 스타일 */
QWidget {
    background-color: #F0F2F5;
    color: #333;
    font-family: 'Malgun Gothic';
}
#MainWindow {
    background-color: #FFFFFF;
}

/* 네비게이션 패널 스타일 */
#nav_panel {
    background-color: #2C3E50;
    border-right: 1px solid #E0E0E0;
}
#title_label {
    background-color: #2C3E50;
    color: #FFFFFF;
    font-size: 24px;
    font-weight: bold;
    padding: 20px;
    text-align: center;
    qproperty-alignment: AlignCenter;
}
#admin_label {
    background-color: #2C3E50;
    color: #D64541;
    font-size: 18px;
    font-weight: bold;
    text-align: center;
    qproperty-alignment: AlignCenter;
}
#NavButton {
    background-color: #2C3E50;
    color: #ECF0F1;
    border: none;
    padding: 15px 20px;
    text-align: left;
    font-size: 16px;
    font-weight: bold;
}
#NavButton:checked {
    background-color: #E74C3C;
    color: #FFFFFF;
}

/* 컨텐츠 영역 스타일 */
#ContentPanel, .QScrollArea {
    background-color: #F0F2F5;
    padding: 10px;
}
#ContentPanel > QLabel, 
#page_robot_management > QVBoxLayout > QLabel, 
#page_task_history > QVBoxLayout > QLabel, 
#page_task_detail > QVBoxLayout > QLabel {
    font-size: 28px;
    font-weight: bold;
    color: #34495E;
    margin-bottom: 10px;
}

/* 버튼 스타일 */
.SearchButton {
    background-color: #D64541;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
}

/* 상태 레이블 스타일 */
.StatusLabel {
    font-size: 12px;
    font-weight: bold;
    padding: 4px 8px;
    border-radius: 4px;
    color: white;
}
.StatusLabel[status="working"] { background-color: #2ECC71; }
.StatusLabel[status="charging"] { background-color: #3498DB; }
.StatusLabel[status="error"] { background-color: #E74C3C; }

/* 카드 스타일 */
#task_detail_card, #SummaryCard {
    background-color: #FFFFFF;
    border-radius: 8px;
    padding: 20px;
}
#SummaryCard QLabel { 
    color: #34495E; 
    text-align: center; 
}
#SummaryCard QLabel[is_title="true"] { 
    font-size: 16px; 
    color: #7F8C8D; 
}
#SummaryCard QLabel[is_value="true"] { 
    font-size: 40px; 
    font-weight: bold; 
}

/* 로봇 관리 카드 */
#RobotCard {
    background-color: #FFFFFF;
    border: 1px solid #E0E0E0;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 10px;
    min-width: 250px;
}
#RobotCard QLabel { 
    background-color: #FFFFFF; 
}
"""

class RobotCard(QFrame):
    def __init__(self, robot_info, parent=None):
        super().__init__(parent)
        self.setObjectName("RobotCard")
        layout = QGridLayout(self)
        header_layout = QHBoxLayout()
        robot_id_label = QLabel(f"<b>{robot_info['id']}</b>")
        robot_id_label.setStyleSheet("font-size: 20px;")
        battery_progress = QProgressBar()
        battery_progress.setValue(robot_info['battery'])
        battery_progress.setTextVisible(True)
        battery_progress.setFixedSize(60, 20)
        if robot_info['battery'] < 20:
             battery_progress.setStyleSheet("QProgressBar::chunk { background-color: #E74C3C; }")
        
        header_layout.addWidget(robot_id_label)
        header_layout.addStretch()
        header_layout.addWidget(battery_progress)
        layout.addLayout(header_layout, 0, 0, 1, 2)
        layout.addWidget(QLabel(robot_info['model']), 1, 0, 1, 2)
        layout.addWidget(QLabel(f"현재 위치 : {robot_info['location']}"), 2, 0, 1, 2)
        layout.addWidget(QLabel(f"작업 : {robot_info['task']}"), 3, 0, 1, 2)
        status_label = QLabel(robot_info['status_text'])
        status_label.setProperty("class", "StatusLabel")
        status_label.setProperty("status", robot_info['status'])
        layout.addWidget(status_label, 4, 0)
        
        if robot_info['error']:
            error_label = QLabel(robot_info['error'])
            error_label.setStyleSheet("color: #E74C3C; font-weight: bold;")
            layout.addWidget(error_label, 4, 1, Qt.AlignmentFlag.AlignRight)


class TimelineItem(QWidget):
    def __init__(self, time, event, is_first=False, is_last=False):
        super().__init__()
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 10, 0, 10)
        line_layout = QVBoxLayout()
        line_layout.setSpacing(0)
        upper_line = QFrame()
        upper_line.setFrameShape(QFrame.Shape.VLine)
        upper_line.setFrameShadow(QFrame.Shadow.Sunken)
        if is_first: upper_line.setVisible(False)
        circle = QLabel("●")
        circle.setStyleSheet("color: #3498DB; font-size: 16px;")
        lower_line = QFrame()
        lower_line.setFrameShape(QFrame.Shape.VLine)
        lower_line.setFrameShadow(QFrame.Shadow.Sunken)
        if is_last: lower_line.setVisible(False)
        line_layout.addWidget(upper_line, alignment=Qt.AlignmentFlag.AlignCenter)
        line_layout.addWidget(circle, alignment=Qt.AlignmentFlag.AlignCenter)
        line_layout.addWidget(lower_line, alignment=Qt.AlignmentFlag.AlignCenter)
        text_layout = QVBoxLayout()
        text_layout.addWidget(QLabel(f"<b>{time}</b>"))
        text_layout.addWidget(QLabel(event))
        layout.addLayout(line_layout)
        layout.addLayout(text_layout, 1)


class AdminApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # ⭐️ UI 파일 로드!
        uic.loadUi("admin_gui.ui", self)
        self.setStyleSheet(STYLESHEET)
        
        # UI 파일에 정의된 위젯에 이벤트 핸들러 및 로직 연결
        self.connect_signals()
        self.load_initial_data()

        # 시작 페이지 설정
        self.dashboard_btn.setChecked(True)

    def connect_signals(self):
        """UI 파일의 위젯과 로직(함수)을 연결합니다."""
        # 네비게이션 버튼과 페이지 전환 연결
        self.dashboard_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.robot_mgmt_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.task_history_btn.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        
        # 상세 보기 버튼 연결
        self.view_detail_btn.clicked.connect(self.view_task_detail)

    def load_initial_data(self):
        """프로그램 시작 시 각 페이지의 데이터를 로드합니다."""
        self.load_dashboard_data()
        self.load_robot_data()
        self.load_task_history_data()

    # --- 대시보드 로직 ---
    def load_dashboard_data(self):
        summary_data = [("총 작업 수", "127"), ("대기 작업 수", "12"), ("활성 로봇 수", "6"), ("오류 수", "3")]
        for i, (text, value) in enumerate(summary_data):
            card = QWidget()
            card.setObjectName("SummaryCard")
            card_layout = QVBoxLayout(card)
            title_label = QLabel(text)
            title_label.setProperty("is_title", "true")
            value_label = QLabel(value)
            value_label.setProperty("is_value", "true")
            card_layout.addWidget(value_label)
            card_layout.addWidget(title_label)
            # 'summary_layout'은 .ui 파일에 정의된 QGridLayout의 objectName
            self.summary_layout.addWidget(card, 0, i)

    # --- 로봇 관리 로직 ---
    def load_robot_data(self):
        mock_robot_data = [
            {'id': 'R-01', 'model': 'RobotBot-V2', 'battery': 98, 'location': '2층 복도', 'task': '#4', 'status': 'working', 'status_text': '작업중', 'error': None},
            {'id': 'R-02', 'model': 'RobotBot-V2', 'battery': 15, 'location': '충전소', 'task': '없음', 'status': 'charging', 'status_text': '충전중', 'error': None},
            {'id': 'R-03', 'model': 'RobotBot-Pro', 'battery': 99, 'location': '대기 구역', 'task': '#5', 'status': 'error', 'status_text': '오류', 'error': '오류 : 충격 감지'},
        ]
        # 'robot_list_layout'은 .ui 파일에 정의된 QHBoxLayout의 objectName
        for robot in mock_robot_data:
            self.robot_list_layout.addWidget(RobotCard(robot))
        self.robot_list_layout.addStretch()

    # --- 작업 이력 로직 ---
    def load_task_history_data(self):
        mock_task_data = [
            ("43", "배송", "완료", "804호", "R-03", "12:02 - 12:12"),
            ("44", "길 안내", "완료", "202호", "R-02", "11:50 - 12:05"),
            ("45", "호출", "완료", "로비", "R-02", "11:01 - 11:12"),
        ]
        # 'task_table'은 .ui 파일에 정의된 QTableWidget의 objectName
        self.task_table.setRowCount(len(mock_task_data))
        for row, data in enumerate(mock_task_data):
            for col, item in enumerate(data):
                self.task_table.setItem(row, col, QTableWidgetItem(item))

    def view_task_detail(self):
        selected_rows = self.task_table.selectionModel().selectedRows()
        if selected_rows:
            task_id = self.task_table.item(selected_rows[0].row(), 0).text()
            self.load_task_detail_data(task_id)
            self.stacked_widget.setCurrentIndex(3) # 상세 페이지로 전환
            self.task_history_btn.setChecked(True)

    # --- 작업 상세 로직 ---
    def load_task_detail_data(self, task_id):
        """작업 상세 정보를 로드하고 표시합니다."""
        # 타이틀 업데이트
        self.task_detail_title_label.setText(f"Task Detail - T-{task_id}")
        
        # 기존 데이터 클리어
        while self.info_grid_layout.count():
            item = self.info_grid_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
                
        while self.timeline_vbox.count():
            item = self.timeline_vbox.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # 작업 상세 정보
        info_data = {
            "Task ID": f"T-{task_id}",
            "작업 종류": "배송",
            "요청자": "804호",
            "배정 로봇": "R-03",
            "상태": "완료",
            "요청 시간": "12:02:00",
            "완료 시간": "12:12:00",
            "소요 시간": "10분"
        }
        
        # 타임라인 데이터
        timeline_data = [
            ("12:02:00", "작업 요청 접수"),
            ("12:05:00", "로봇 할당"),
            ("12:07:00", "목적지 도착"),
            ("12:12:00", "배송 완료")
        ]
        
        # 정보 그리드에 데이터 추가
        for row, (key, value) in enumerate(info_data.items()):
            # 레이블 생성
            key_label = QLabel(f"<b>{key}</b>")
            key_label.setStyleSheet("color: #2C3E50;")
            value_label = QLabel(value)
            
            # 상태 레이블 스타일 지정
            if key == "상태":
                if value == "완료":
                    value_label.setStyleSheet("color: #2ECC71; font-weight: bold;")
                elif value == "진행중":
                    value_label.setStyleSheet("color: #3498DB; font-weight: bold;")
                elif value == "대기":
                    value_label.setStyleSheet("color: #F1C40F; font-weight: bold;")
                elif value == "실패":
                    value_label.setStyleSheet("color: #E74C3C; font-weight: bold;")
            
            # 그리드에 위젯 추가
            self.info_grid_layout.addWidget(key_label, row, 0)
            self.info_grid_layout.addWidget(value_label, row, 1)
        
        # 타임라인 데이터 추가
        for i, (time, event) in enumerate(timeline_data):
            timeline_item = TimelineItem(
                time, 
                event,
                is_first=(i == 0),
                is_last=(i == len(timeline_data) - 1)
            )
            self.timeline_vbox.addWidget(timeline_item)
        
        # 타임라인 끝에 여백 추가
        self.timeline_vbox.addStretch()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdminApp()
    window.show()
    sys.exit(app.exec())