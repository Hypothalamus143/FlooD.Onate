document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelectorAll('.messages li');
    messages.forEach(function(msg) {
        // Remove from DOM after 5.5 seconds (matches CSS animation)
        setTimeout(function() {
            if (msg.parentNode) {
                msg.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
                msg.style.opacity = '0';
                msg.style.transform = 'translateX(50px)';
                setTimeout(function() {
                    if (msg.parentNode) {
                        msg.remove();
                        // Remove empty messages container
                        const container = document.querySelector('.messages');
                        if (container && container.children.length === 0) {
                            container.remove();
                        }
                    }
                }, 400);
            }
        }, 5500);
    });
});
