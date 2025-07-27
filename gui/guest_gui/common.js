// common.js

// -----------------------------------------------------------
// 💡 getLocationName 함수 (DOMContentLoaded 외부에서 정의하여 전역 접근 가능하게 함)
// -----------------------------------------------------------
window.common = {
    getLocationName: function(locationCode) {
        if (locationCode === "ROOM_201") {
            return "201호";
        }
        if (locationCode === "ROOM_102") { // 예시: ROOM_102 추가
            return "102호";
        }
        // 필요한 모든 위치 코드에 대해 매핑을 추가하거나 서버 응답을 직접 활용하세요.
        return locationCode; // 매핑된 이름이 없으면 코드 그대로 반환
    }
};


// -----------------------------------------------------------
// 💡 showToast 함수 (전역으로 바로 사용 가능하도록 정의)
// -----------------------------------------------------------
window.showToast = function(imagePath, type = 'default') {
    const toast = document.getElementById('global-toast');
    const fullImageElement = document.getElementById('toast-full-image');

    if (!toast || !fullImageElement) return;

    fullImageElement.src = imagePath;
    fullImageElement.alt = '';

    toast.className = 'global-toast';
    toast.classList.add(type);     // 'success', 'error' 등
    toast.classList.remove('hidden');

    setTimeout(() => {
        toast.classList.add('hidden');
        fullImageElement.src = '';
    }, 3000);
}

// -----------------------------------------------------------
// 💡 DOMContentLoaded: 페이지 로드 후 실행될 공통 로직
// -----------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {

    // 1. 헤더의 방 번호 동적 설정 (모든 페이지의 .room-number에 적용)
    const roomNumberElements = document.querySelectorAll('.room-number'); // querySelectorAll로 변경
    if (roomNumberElements.length > 0 && typeof CONFIG !== 'undefined' && CONFIG.DEFAULT_ROOM_ID) {
        roomNumberElements.forEach(element => {
            element.textContent = CONFIG.DEFAULT_ROOM_ID;
        });
    }

    // 2. 뒤로가기 버튼 기능 (back_button_1 ID를 사용하는 모든 요소에 적용)
    const backButtonGlobal = document.getElementById('back_button_1');
    if (backButtonGlobal && !backButtonGlobal._hasListener) { // 중복 리스너 방지
        backButtonGlobal.addEventListener('click', () => {
            window.history.back();
        });
        backButtonGlobal._hasListener = true;
    }

    // 3. 전역 토스트 알림 DOM 요소 확인 (HTML에 직접 삽입되어 있다면 이 코드는 제거)
    // 현재 모든 HTML 파일에 <div id="global-toast">...</div>가 직접 추가되어 있으므로 이 블록은 제거해야 합니다.
    // if (!document.getElementById('global-toast')) {
    //     const globalToastHtml = `
    //         <div id="global-toast" class="global-toast hidden">
    //             <img id="toast-full-image" class="toast-image" src="" alt="Notification">
    //         </div>
    //     `;
    //     document.body.insertAdjacentHTML('beforeend', globalToastHtml);
    // }


    // -----------------------------------------------------------
    // 💡 WebSocket 연결 로직 (DOMContentLoaded 내부에서 정의하여 CONFIG 객체에 접근 가능하게 함)
    // -----------------------------------------------------------
    // 이 WebSocket 로직은 common.js에서 한 번만 초기화되어야 합니다.
    // 중복 연결을 피하기 위해 `window.webSocketInitialized`와 같은 플래그를 사용할 수 있습니다.
    if (typeof CONFIG !== 'undefined' && CONFIG.WS_BASE_URL && !window.webSocketInitialized) {
        let socket;
        let reconnectInterval = null; // null로 초기화
        const RECONNECT_DELAY = 5000; // 5초 후 재연결 시도

        function connectWebSocket() {
            if (socket && (socket.readyState === WebSocket.OPEN || socket.readyState === WebSocket.CONNECTING)) {
                console.log("WebSocket이 이미 열려 있거나 연결 중입니다. 새로운 연결 시도를 건너뜝니다.");
                return;
            }

            console.log(`WebSocket 연결 시도 중: ${CONFIG.WS_BASE_URL}`); // 연결 시도 시 URL 로깅
            socket = new WebSocket(CONFIG.WS_BASE_URL);

            socket.addEventListener("open", (event) => {
                console.log("WebSocket 연결됨:", event);
                if (reconnectInterval) { // reconnectInterval이 설정되어 있을 경우에만 클리어
                    clearInterval(reconnectInterval);
                    reconnectInterval = null;
                    console.log("재연결 인터벌이 제거되었습니다.");
                }
            });

            socket.addEventListener("message", (event) => {
                try {
                    const data = JSON.parse(event.data);
                    console.log("WebSocket 메시지 수신:", data);

                    if (data.type === "event") {
                        switch (data.action) {
                            case "task_timeout_return":
                                showToast('asset/timeout_return_notification.png');
                                break;
                            case "delivery_completion":
                                showToast('asset/delivery_completed_notification.png');
                                break;
                            case "robot_arrival_completion":
                                showToast('asset/robot_arrived_pickup.png');
                                break;
                            case "call_request_acceptance":
                                showToast('asset/call_accepted.png');
                                break;
                            default:
                                console.warn("알 수 없는 이벤트 액션:", data.action);
                        }
                    } else if (data.type === "response") {
                        console.log("응답 메시지 (WebSocket):", data);
                    }
                } catch (e) {
                    console.error("WebSocket 메시지 파싱 오류:", e, "원본 데이터:", event.data); // 원본 데이터 추가
                    showToast('asset/error_toast.png', 'error'); // WebSocket 메시지 파싱 오류 토스트
                }
            });

            socket.addEventListener("close", (event) => {
                console.warn(`WebSocket 연결 끊김. 코드: ${event.code}, 이유: ${event.reason}`); // 상세한 종료 메시지
                showToast('asset/error_toast.png', 'error'); // WebSocket 연결 끊김 토스트
                if (!reconnectInterval) {
                    console.log(`${RECONNECT_DELAY / 1000}초 후에 재연결을 시도합니다...`); // 재연결 시도 메시지
                    reconnectInterval = setInterval(connectWebSocket, RECONNECT_DELAY);
                }
            });

            socket.addEventListener("error", (event) => {
                console.error("WebSocket 오류 발생:", event);
                showToast('asset/error_toast.png', 'error'); // WebSocket 오류 토스트
                // 오류 발생 시 소켓이 이미 닫히고 있을 수 있지만, 명시적으로 닫아 close 이벤트가 발생하도록 보장
                if (socket.readyState === WebSocket.OPEN || socket.readyState === WebSocket.CONNECTING) {
                    socket.close();
                }
            });
        }

        connectWebSocket();
        window.webSocketInitialized = true;
        window.socket = socket; // socket 객체를 전역으로 노출하여 다른 페이지에서 접근 가능하게 함
    }
    else
        {
        console.warn("CONFIG에 WebSocket URL이 정의되지 않았거나 WebSocket이 이미 초기화되었습니다. WS 기능이 비활성화됩니다.");
    }
});