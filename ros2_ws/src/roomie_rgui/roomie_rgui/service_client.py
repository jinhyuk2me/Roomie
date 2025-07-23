import threading
import rclpy

def call_service(node, client, request):
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info("서비스 대기 중...")

    future = client.call_async(request)

    def _callback():
        rclpy.spin_until_future_complete(node, future)
        if future.result():
            node.get_logger().info(f"[서비스 응답] {future.result()}")
        else:
            node.get_logger().error("[서비스 실패]")

    threading.Thread(target=_callback).start()
