// subscription.js
document.addEventListener('DOMContentLoaded', function() {
    // 필요한 DOM 요소들을 가져옵니다
    const subscribeButton = document.getElementById('subscribeButton');
    const subscriberCount = document.getElementById('subscriberCount');

    if (subscribeButton) {
        subscribeButton.addEventListener('click', async function() {
            // 버튼 데이터에서 게시물 ID를 가져옵니다
            const postId = this.dataset.postId;
            // CSRF 토큰을 가져옵니다
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            try {
                // 중복 클릭 방지를 위해 버튼을 비활성화합니다
                this.disabled = true;

                // 서버에 구독 요청을 보냅니다
                const response = await fetch(`/imageapp/image/${postId}/subscribe/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrfToken,
                        'Content-Type': 'application/json',
                    },
                    credentials: 'same-origin'
                });

                if (!response.ok) {
                    throw new Error('서버 응답 오류');
                }

                const data = await response.json();

                // 응답 데이터에 따라 UI를 업데이트합니다
                if (data.status === 'subscribed') {
                    subscribeButton.textContent = '구독 중';
                } else {
                    subscribeButton.textContent = '구독하기';
                }

                // 구독자 수를 업데이트합니다
                subscriberCount.textContent = `구독자 ${data.subscriber_count}명`;

                // 사용자에게 결과를 알립니다
                // alert(data.message);

            } catch (error) {
                console.error('Error:', error);
                // alert('오류가 발생했습니다. 다시 시도해주세요.');
            } finally {
                // 작업이 완료되면 버튼을 다시 활성화합니다
                this.disabled = false;
            }
        });
    }
});
