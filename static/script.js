document.addEventListener('DOMContentLoaded', function() {
    function createBubble() {
        const bubble = document.createElement('div');
        bubble.className = 'bubble';
        const size = Math.random() * 60 + 20 + 'px';
        bubble.style.width = size;
        bubble.style.height = size;
        bubble.style.left = Math.random() * 100 + 'vw';
        bubble.style.top = Math.random() * 80 + 'vh'; // スタート位置を上に調整
        bubble.style.backgroundColor = getRandomColor();
        bubble.style.opacity = Math.random() * 0.5 + 0.5; // 透明度を設定

        document.getElementById('bubbles').appendChild(bubble);

        setTimeout(() => {
            bubble.remove();
        }, 15000); // シャボン玉の寿命を短くする
    }

    function getRandomColor() {
        const colors = ['#FF69B4', '#FFD700', '#FF4500', '#7FFF00', '#1E90FF', '#8A2BE2', '#00CED1'];
        return colors[Math.floor(Math.random() * colors.length)];
    }

    setInterval(createBubble, 500); // シャボン玉の出現間隔を短くする
});
