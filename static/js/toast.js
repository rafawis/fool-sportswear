(function () {
    const toastComponent = document.getElementById('toast-component');
    const toastIcon = document.getElementById('toast-icon');
    const toastTitle = document.getElementById('toast-title');

    // Bikin kelas untuk sukses dan error
    const typeClasses = {
        'success': {
            icon: '✔',
            iconClasses: 'text-purple-600',
            title: 'Success',
        },
        'error': {
            icon: '✖',
            iconClasses: 'text-red-600',
            title: 'Error',
        },
    };

    let toastTimeout = null;

    // hapus kelas icon yang udah ada secara default
    function clearIconClasses(element) {
        const classesToRemove = [
            'text-green-600', 'text-red-600', 'text-blue-600'
        ];
        element.classList.remove(...classesToRemove);
    }

    function clearBgClasses(element) {
    const bgClassesToRemove = [
        'bg-green-50', 'bg-red-50', 'bg-blue-50', 'bg-purple-50', 'bg-white'
    ];
    element.classList.remove(...bgClassesToRemove);
}

window.showToast = function (title, message, type = 'info', duration = 4000) {
    clearBgClasses(toastComponent);

    if (type === 'success') {
        toastComponent.classList.add('bg-purple-300');
    } else if (type === 'error') {
        toastComponent.classList.add('bg-red-50');
    } else {
        toastComponent.classList.add('bg-white');
    }
        if (toastTimeout) {
            clearTimeout(toastTimeout);
        }
        clearIconClasses(toastIcon);

        const config = typeClasses[type] || typeClasses['info'];

        toastTitle.textContent = title || config.title;
        document.getElementById('toast-message').textContent = message;

        toastIcon.textContent = config.icon;
        toastIcon.classList.add(...config.iconClasses.split(' '));

        toastComponent.classList.remove('translate-y-64', 'opacity-0');
        toastComponent.classList.add('opacity-100');

        toastTimeout = setTimeout(() => {
            toastComponent.classList.remove('opacity-100');
            toastComponent.classList.add('translate-y-64', 'opacity-0');
        }, duration);
    };
})();