// mi_animacion.js

// Llama a la biblioteca LottieWeb
import lottie from 'https://cdn.jsdelivr.net/npm/lottie-web/build/player/lottie_light.min.js';

// Configuración de la animación
var animacionConfig = {
    container: document.getElementById('animation-container'),
    renderer: 'svg',
    loop: true,
    autoplay: true,
    path: '/Animation-1706015468852.json' // Reemplaza con la ruta correcta a tu archivo JSON de animación Lottie
};

// Cargar la animación
var animacion = lottie.loadAnimation(animacionConfig);
