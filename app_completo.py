from flask import Flask, render_template_string, session, request, jsonify
import random
import time

app = Flask(__name__)
app.secret_key = 'lectolandia-secret-key-2024'

# Datos exactos de tu código React
palabras_completas = {
    'es': {
        1: [
            'sol', 'mar', 'luz', 'flor', 'pez', 'rey', 'león', 'dos', 'tres', 'mes',
            'gato', 'can', 'oso', 'buey', 'pato', 'loro', 'ratón', 'pájaro', 'zorro', 'ciervo',
            'pan', 'sal', 'miel', 'té', 'uva', 'pera', 'nuez', 'col', 'ajo', 'flan',
            'pie', 'mano', 'ojo', 'nariz', 'boca', 'diente', 'pelo', 'piel', 'hueso', 'sangre',
            'techo', 'pared', 'puerta', 'mesa', 'silla', 'cama', 'baño', 'cocina', 'sala', 'jardín',
            'libro', 'lápiz', 'papel', 'coche', 'tren', 'globo', 'pelota', 'muñeca', 'juego', 'reloj',
            'amor', 'paz', 'fe', 'bien', 'mal', 'risa', 'llanto', 'miedo', 'susto', 'sorpresa'
        ],
        2: [
            'mamá', 'papá', 'niña', 'niño', 'bebé', 'tata', 'yaya', 'primo', 'tío', 'hermano',
            'gato', 'perro', 'vaca', 'cabra', 'oveja', 'pollo', 'pato', 'conejo', 'mono', 'tigre',
            'burro', 'cebra', 'rana', 'panda', 'koala', 'puma', 'lobo', 'foca', 'pulpo', 'águila',
            'casa', 'mesa', 'silla', 'cama', 'sofá', 'baño', 'cocina', 'puerta', 'ventana', 'techo',
            'jardín', 'patio', 'garage', 'sala', 'cuarto', 'pasillo', 'escalón', 'balcón', 'terraza', 'chimenea',
            'agua', 'leche', 'jugo', 'sopa', 'pasta', 'pizza', 'queso', 'huevo', 'carne', 'pollo',
            'pescado', 'fruta', 'verdura', 'arroz', 'fideo', 'dulce', 'helado', 'torta', 'galleta', 'chocolate',
            'luna', 'tierra', 'cielo', 'nube', 'lluvia', 'nieve', 'viento', 'río', 'lago', 'monte',
            'árbol', 'planta', 'césped', 'arena', 'piedra', 'roca', 'isla', 'playa', 'bosque', 'selva',
            'rojo', 'azul', 'verde', 'negro', 'blanco', 'rosa', 'gris', 'café', 'dorado', 'plateado'
        ],
        3: [
            'mariposa', 'elefante', 'jirafa', 'hipopótamo', 'cocodrilo', 'serpiente', 'tortuga', 'libélula', 'caracol', 'abejorro',
            'guitarra', 'piano', 'tambor', 'flauta', 'trompeta', 'violín', 'micrófono', 'altavoz', 'cámara', 'televisor',
            'computadora', 'teléfono', 'refrigerador', 'lavadora', 'aspiradora', 'tostadora', 'batidora', 'licuadora', 'cafetera', 'plancha',
            'ventana', 'escalera', 'armario', 'estante', 'alfombra', 'cortina', 'almohada', 'manta', 'espejo', 'lámpara',
            'montaña', 'volcán', 'cascada', 'arroyo', 'pradera', 'desierto', 'glaciar', 'pantano', 'laguna', 'manantial',
            'banana', 'manzana', 'naranja', 'sandía', 'piña', 'frutilla', 'cereza', 'durazno', 'ciruela', 'mandarina',
            'automóvil', 'bicicleta', 'motocicleta', 'helicóptero', 'submarino', 'ambulancia', 'bomberos', 'policía', 'camión', 'autobús',
            'doctora', 'maestra', 'bombero', 'policía', 'cocinero', 'jardinero', 'carpintero', 'plomero', 'electricista', 'veterinario'
        ]
    },
    'ca': {
        1: [
            'sol', 'mar', 'llum', 'flor', 'peix', 'rei', 'lleó', 'dos', 'tres', 'mes',
            'gat', 'gos', 'ós', 'bou', 'ànec', 'lloro', 'ratolí', 'ocell', 'guineu', 'cérvol',
            'pa', 'sal', 'mel', 'té', 'raïm', 'pera', 'nou', 'col', 'all', 'flam',
            'peu', 'mà', 'ull', 'nas', 'boca', 'dent', 'pèl', 'pell', 'os', 'sang',
            'sostre', 'paret', 'porta', 'taula', 'cadira', 'llit', 'bany', 'cuina', 'sala', 'jardí',
            'llibre', 'llapis', 'paper', 'cotxe', 'tren', 'globus', 'pilota', 'nina', 'joc', 'rellotge',
            'amor', 'pau', 'fe', 'bé', 'mal', 'riure', 'plor', 'por', 'ensurt', 'sorpresa'
        ],
        2: [
            'mare', 'pare', 'nena', 'nen', 'bebè', 'tata', 'iaia', 'cosí', 'oncle', 'germà',
            'gat', 'gos', 'vaca', 'cabra', 'ovella', 'pollastre', 'ànec', 'conill', 'mico', 'tigre',
            'casa', 'taula', 'cadira', 'llit', 'sofà', 'bany', 'cuina', 'porta', 'finestra', 'sostre',
            'aigua', 'llet', 'suc', 'sopa', 'pasta', 'pizza', 'formatge', 'ou', 'carn', 'pollastre',
            'lluna', 'terra', 'cel', 'núvol', 'pluja', 'neu', 'vent', 'riu', 'llac', 'mont',
            'arbre', 'planta', 'gespa', 'sorra', 'pedra', 'roca', 'illa', 'platja', 'bosc', 'selva',
            'vermell', 'blau', 'verd', 'negre', 'blanc', 'rosa', 'gris', 'marró', 'daurat', 'platejat'
        ],
        3: [
            'papallona', 'elefant', 'girafa', 'hipopòtam', 'cocodril', 'serpent', 'tortuga', 'libèl·lula', 'caragol', 'borinot',
            'guitarra', 'piano', 'tambor', 'flauta', 'trompeta', 'violí', 'micròfon', 'altaveu', 'càmera', 'televisor',
            'ordinador', 'telèfon', 'nevera', 'rentadora', 'aspiradora', 'torradora', 'batedora', 'liquadora', 'cafetera', 'planxa',
            'finestra', 'escalera', 'armari', 'prestatge', 'catifa', 'cortina', 'coixí', 'manta', 'mirall', 'llàntia',
            'muntanya', 'volcà', 'cascada', 'rierol', 'pradera', 'desert', 'glacera', 'pantà', 'llacuna', 'deu',
            'plàtan', 'poma', 'taronja', 'síndria', 'pinya', 'maduixa', 'cirera', 'préssec', 'pruna', 'mandarina',
            'automòbil', 'bicicleta', 'motocicleta', 'helicòpter', 'submarí', 'ambulància', 'bombers', 'policia', 'camió', 'autobús'
        ]
    }
}

# Sistema de badges exacto
badges = {
    'es': [
        {'id': 'twenty_read', 'name': 'Lectora Constante', 'description': 'Has leído 20 palabras', 'icon': '🌟', 'threshold': 20, 'theme': 'yellow'},
        {'id': 'forty_read', 'name': 'Lectora Dedicada', 'description': 'Has leído 40 palabras', 'icon': '🚀', 'threshold': 40, 'theme': 'blue'},
        {'id': 'sixty_read', 'name': 'Lectora Experta', 'description': 'Has leído 60 palabras', 'icon': '⚡', 'threshold': 60, 'theme': 'purple'},
        {'id': 'eighty_read', 'name': 'Súper Lectora', 'description': 'Has leído 80 palabras', 'icon': '🦸‍♀️', 'threshold': 80, 'theme': 'pink'},
        {'id': 'marathon', 'name': 'Lectora Maratón', 'description': 'Practicaste 10 minutos', 'icon': '🏃‍♀️', 'threshold': 600, 'theme': 'green'},
        {'id': 'hundred_club', 'name': 'Campeona', 'description': 'Leíste 100 palabras', 'icon': '👑', 'threshold': 100, 'theme': 'gold'},
        {'id': 'master_reader', 'name': 'Maestra de Lectura', 'description': 'Has leído 120 palabras', 'icon': '💫', 'threshold': 120, 'theme': 'rainbow'}
    ],
    'ca': [
        {'id': 'twenty_read', 'name': 'Lectora Constant', 'description': 'Has llegit 20 paraules', 'icon': '🌟', 'threshold': 20, 'theme': 'yellow'},
        {'id': 'forty_read', 'name': 'Lectora Dedicada', 'description': 'Has llegit 40 paraules', 'icon': '🚀', 'threshold': 40, 'theme': 'blue'},
        {'id': 'sixty_read', 'name': 'Lectora Experta', 'description': 'Has llegit 60 paraules', 'icon': '⚡', 'threshold': 60, 'theme': 'purple'},
        {'id': 'eighty_read', 'name': 'Súper Lectora', 'description': 'Has llegit 80 paraules', 'icon': '🦸‍♀️', 'threshold': 80, 'theme': 'pink'},
        {'id': 'marathon', 'name': 'Lectora Marató', 'description': 'Vas practicar 10 minuts', 'icon': '🏃‍♀️', 'threshold': 600, 'theme': 'green'},
        {'id': 'hundred_club', 'name': 'Campiona', 'description': 'Vas llegir 100 paraules', 'icon': '👑', 'threshold': 100, 'theme': 'gold'},
        {'id': 'master_reader', 'name': 'Mestra de Lectura', 'description': 'Has llegit 120 paraules', 'icon': '💫', 'threshold': 120, 'theme': 'rainbow'}
    ]
}
themes = {
    'default': 'from-purple-400 via-pink-400 to-blue-400',
    'yellow': 'from-yellow-300 via-orange-300 to-red-400',
    'blue': 'from-blue-400 via-cyan-400 to-teal-400',
    'purple': 'from-purple-500 via-indigo-500 to-blue-500',
    'pink': 'from-pink-400 via-rose-400 to-red-400',
    'green': 'from-green-400 via-emerald-400 to-teal-400',
    'gold': 'from-yellow-400 via-amber-400 to-orange-400',
    'rainbow': 'from-pink-400 via-purple-400 via-indigo-400 via-blue-400 via-green-400 to-yellow-400'
}

def generar_silabas():
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    vowels = ['A', 'E', 'I', 'O', 'U']
    special_combos = ['ch', 'll', 'rr', 'bl', 'br', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'tr']
    
    syllables = []
    for consonant in consonants:
        for vowel in vowels:
            syllables.append((consonant + vowel).lower())
    
    for combo in special_combos:
        for vowel in vowels:
            syllables.append((combo + vowel.lower()))
    
    return syllables

def generar_item(mode, syllable_count, language):
    if mode == 'syllables':
        all_syllables = generar_silabas()
        if syllable_count == 1:
            return random.choice(all_syllables)
        else:
            item = ''
            for _ in range(syllable_count):
                item += random.choice(all_syllables)
            return item
    else:
        words = palabras_completas[language].get(syllable_count, palabras_completas[language][2])
        return random.choice(words)

def get_pet_mood(read_count):
    if read_count >= 80:
        return 'excited'
    elif read_count >= 40:
        return 'happy'
    elif read_count >= 20:
        return 'normal'
    else:
        return 'sleepy'

def get_pet_emoji(mood):
    emojis = {'excited': '🤩', 'happy': '😊', 'normal': '😐', 'sleepy': '😴'}
    return emojis.get(mood, '😴')

def get_pet_message(mood, language):
    messages = {
        'es': {'excited': '¡Increíble progreso!', 'happy': '¡Muy bien!', 'normal': '¡Sigue practicando!', 'sleepy': 'Comencemos a leer...'},
        'ca': {'excited': '¡Progrés increïble!', 'happy': '¡Molt bé!', 'normal': '¡Continua practicant!', 'sleepy': 'Comencem a llegir...'}
    }
    return messages.get(language, messages['es']).get(mood, 'Comencemos...')

def check_badges(read_count, total_time, current_badge, language):
    if read_count < 20 or read_count % 20 != 0:
        return None
    
    current_badges = badges[language]
    highest_badge = None
    highest_value = 0
    
    for badge in current_badges:
        earned = False
        if badge['id'] in ['twenty_read', 'forty_read', 'sixty_read', 'eighty_read', 'hundred_club', 'master_reader']:
            earned = read_count >= badge['threshold']
        elif badge['id'] == 'marathon':
            earned = total_time >= badge['threshold']
        
        if earned and badge['threshold'] > highest_value:
            highest_badge = badge
            highest_value = badge['threshold']
    
    if highest_badge and (not current_badge or highest_badge['id'] != current_badge.get('id')):
        return highest_badge
    return None

# Template HTML exacto a tu React
template = '''
<!DOCTYPE html>
<html lang="es">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>LectoLandia</title>
   <script src="https://cdn.tailwindcss.com"></script>
   <style>
       @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
       body { 
           font-family: 'Inter', sans-serif;
       }
       .animate-bounce { animation: bounce 1s infinite; }
       @keyframes bounce { 0%, 20%, 53%, 80%, 100% { transform: translateY(0); } 40%, 43% { transform: translateY(-20px); } 70% { transform: translateY(-10px); } }
       .transition-all { transition: all 0.3s ease; }
       .backdrop-blur { backdrop-filter: blur(10px); }
   </style>
</head>
<body class="min-h-screen transition-all duration-1000" style="background: linear-gradient(135deg, {{ theme_gradient }}) !important; background-attachment: fixed !important;">
   
   <!-- Notificación de nueva etiqueta -->
   {% if new_badge %}
   <div id="badge-notification" class="fixed top-20 right-4 z-40 bg-white rounded-xl shadow-xl p-4 border-2 border-yellow-400 max-w-xs">
       <div class="text-center">
           <div class="text-3xl mb-1">{{ new_badge.icon }}</div>
           <div class="font-bold text-sm text-gray-800 mb-1">¡Nueva Etiqueta!</div>
           <div class="font-bold text-xs text-purple-600">{{ new_badge.name }}</div>
       </div>
   </div>
   <script>
       setTimeout(() => {
           const notification = document.getElementById('badge-notification');
           if (notification) notification.style.display = 'none';
       }, 3000);
   </script>
   {% endif %}

   <div class="max-w-4xl mx-auto p-4">
       <div class="bg-white rounded-2xl shadow-xl p-6 mb-6 backdrop-blur">
           <div class="flex items-center justify-between mb-4">
               <div class="flex items-center gap-3">
                   <div class="h-8 w-8 text-purple-600">📚</div>
                   <h1 class="text-2xl font-bold text-gray-800">LectoLandia</h1>
               </div>
               <div class="flex items-center gap-4">
                   <div class="flex items-center gap-4 bg-gradient-to-r from-purple-100 to-pink-100 rounded-xl p-3">
                       <div class="text-center">
                           <div class="text-2xl font-bold text-purple-600">{{ level }}</div>
                           <div class="text-xs text-gray-600">Nivel</div>
                       </div>
                       <div class="text-center">
                           <div class="text-2xl font-bold text-pink-600">{{ points }}</div>
                           <div class="text-xs text-gray-600">Puntos</div>
                       </div>
                       <div class="text-center">
                           <div class="text-2xl font-bold text-blue-600">{% if current_badge %}🏷️{% else %}😴{% endif %}</div>
                           <div class="text-xs text-gray-600">Etiqueta</div>
                       </div>
                   </div>
                   <button onclick="toggleSettings()" class="p-2 text-gray-600 hover:bg-gray-100 rounded-lg">⚙️</button>
               </div>
           </div>

           <div id="settings" class="border-t pt-4 mt-4" style="display: {% if show_settings %}block{% else %}none{% endif %};">
               <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                   <div>
                       <label class="block text-sm font-medium text-gray-700 mb-2">Idioma:</label>
                       <select onchange="updateConfig()" id="language" class="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500">
                           <option value="es" {% if language == 'es' %}selected{% endif %}>Español</option>
                           <option value="ca" {% if language == 'ca' %}selected{% endif %}>Català</option>
                       </select>
                   </div>
                   <div>
                       <label class="block text-sm font-medium text-gray-700 mb-2">Modo de práctica:</label>
                       <select onchange="updateConfig()" id="mode" class="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500">
                           <option value="syllables" {% if mode == 'syllables' %}selected{% endif %}>Sílabas</option>
                           <option value="words" {% if mode == 'words' %}selected{% endif %}>Palabras</option>
                       </select>
                   </div>
                   <div>
                       <label class="block text-sm font-medium text-gray-700 mb-2">
                           {% if mode == 'syllables' %}Número de sílabas:{% else %}Tipo de palabras:{% endif %}
                       </label>
                       <select onchange="updateConfig()" id="syllable_count" class="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500">
                           <option value="1" {% if syllable_count == 1 %}selected{% endif %}>
                               {% if mode == 'syllables' %}1 sílaba{% else %}Palabras cortas{% endif %}
                           </option>
                           <option value="2" {% if syllable_count == 2 %}selected{% endif %}>
                               {% if mode == 'syllables' %}2 sílabas{% else %}Palabras medianas{% endif %}
                           </option>
                           <option value="3" {% if syllable_count == 3 %}selected{% endif %}>
                               {% if mode == 'syllables' %}3 sílabas{% else %}Palabras largas{% endif %}
                           </option>
                       </select>
                   </div>
               </div>
           </div>
       </div>

       <div class="grid grid-cols-1 lg:grid-cols-4 gap-6 mb-6">
           <div class="lg:col-span-1">
               <div class="text-center p-4 rounded-2xl transition-all duration-500 {% if current_badge %}{{ get_badge_styles(current_badge.theme) }}{% else %}bg-gradient-to-r from-gray-100 to-gray-200{% endif %}">
                   <div class="text-6xl mb-2 animate-bounce">{{ pet_emoji }}</div>
                   {% if current_badge %}
                       <div class="mb-2">
                           <div class="text-2xl mb-1">{{ current_badge.icon }}</div>
                           <div class="font-bold text-sm text-gray-800">{{ current_badge.name }}</div>
                           <div class="text-xs text-gray-600">{{ current_badge.description }}</div>
                       </div>
                   {% else %}
                       <div class="text-sm text-gray-600 font-medium mb-2">
                           ¡Comienza a leer para desbloquear etiquetas!
                       </div>
                   {% endif %}
                   <div class="text-sm text-purple-700 font-medium">{{ pet_message }}</div>
               </div>
           </div>
           
           <div class="lg:col-span-3 bg-white rounded-2xl shadow-xl p-8 backdrop-blur">
               <div class="text-center mb-8">
                   <div class="bg-gradient-to-r from-purple-100 to-pink-100 rounded-2xl p-8 mb-6 relative overflow-hidden">
                       <div class="relative z-10">
                           <div class="text-6xl font-bold text-gray-800 mb-2 font-mono transition-all duration-300">{{ current_item }}</div>
                           <div class="text-lg text-gray-600">
                               {% if mode == 'syllables' %}
                                   {{ syllable_count }} {% if syllable_count > 1 %}sílabas{% else %}sílaba{% endif %}
                               {% else %}
                                   Palabra de {{ current_item|length }} letras
                               {% endif %}
                           </div>
                       </div>
                   </div>

                   <div class="flex justify-center gap-4">
                       <button onclick="toggleTimer()" id="timer-btn" class="flex items-center gap-2 px-6 py-3 rounded-xl font-semibold transition-all duration-300 transform hover:scale-105 {% if is_playing %}bg-red-500 hover:bg-red-600{% else %}bg-green-500 hover:bg-green-600{% endif %} text-white shadow-lg">
                           <span id="timer-icon">{% if is_playing %}⏸️{% else %}▶️{% endif %}</span>
                           <span id="timer-text">{% if is_playing %}Pausar{% else %}Iniciar{% endif %}</span>
                       </button>
                       <button onclick="nextItem()" class="bg-blue-500 hover:bg-blue-600 text-white px-6 py-3 rounded-xl font-semibold transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl">
                           Siguiente →
                       </button>
                       <button onclick="resetStats()" class="flex items-center gap-2 bg-gray-500 hover:bg-gray-600 text-white px-6 py-3 rounded-xl font-semibold transition-all duration-300 transform hover:scale-105 shadow-lg">
                           🔄 Reiniciar
                       </button>
                   </div>
               </div>
           </div>
       </div>

       <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
           <div class="bg-white rounded-2xl shadow-xl p-6 transform transition-all duration-300 hover:scale-105 backdrop-blur">
               <div class="flex items-center gap-3 mb-2">
                   <span class="text-2xl">⏰</span>
                   <h3 class="text-lg font-semibold text-gray-800">Tiempo Total</h3>
               </div>
               <div class="text-3xl font-bold text-blue-600" id="time-display">{{ time_formatted }}</div>
               <div class="text-sm text-gray-500">minutos</div>
               <div class="mt-3 h-2 bg-gray-200 rounded-full overflow-hidden">
                   <div class="h-full bg-blue-500 transition-all duration-500" style="width: {{ time_progress }}%"></div>
               </div>
           </div>

           <div class="bg-white rounded-2xl shadow-xl p-6 transform transition-all duration-300 hover:scale-105 backdrop-blur">
               <div class="flex items-center gap-3 mb-2">
                   <span class="text-2xl">📚</span>
                   <h3 class="text-lg font-semibold text-gray-800">Lecturas</h3>
               </div>
               <div class="text-3xl font-bold text-green-600">{{ read_count }}</div>
               <div class="text-sm text-gray-500">completadas</div>
               <div class="mt-3 h-2 bg-gray-200 rounded-full overflow-hidden">
                   <div class="h-full bg-green-500 transition-all duration-500" style="width: {{ read_progress }}%"></div>
               </div>
           </div>
       </div>

       {% if motivational_message %}
       <div class="bg-white rounded-2xl shadow-xl p-6 mt-6 backdrop-blur">
           <div class="text-center p-3 bg-gradient-to-r from-blue-50 to-purple-50 rounded-xl">
               <div class="text-lg font-medium text-gray-700">{{ motivational_message }}</div>
           </div>
       </div>
       {% endif %}
   </div>

   <script>
       let isPlaying = {{ is_playing|tojson }};
       let startTime = {{ start_time or 'null' }};
       let totalTime = {{ total_time }};

       function toggleSettings() {
           const settings = document.getElementById('settings');
           settings.style.display = settings.style.display === 'none' ? 'block' : 'none';
       }

       function toggleTimer() {
           fetch('/toggle_timer', { method: 'POST' })
               .then(response => response.json())
               .then(data => {
                   isPlaying = data.is_playing;
                   startTime = data.start_time;
                   updateTimerButton();
               });
       }

       function nextItem() {
    fetch('/next_item', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Actualizar contenido
                document.querySelector('.text-6xl.font-bold').textContent = data.new_item;
                document.querySelector('.text-2xl.font-bold.text-purple-600').textContent = data.level;
                document.querySelector('.text-2xl.font-bold.text-pink-600').textContent = data.points;
                document.querySelector('.text-3xl.font-bold.text-green-600').textContent = data.read_count;
                
                // Cambiar fondo según tema
                const themeGradient = data.theme_gradient;
                if (themeGradient.includes('yellow')) {
                    document.body.style.background = 'linear-gradient(135deg, #fde68a, #fed7aa, #f87171)';
                } else if (themeGradient.includes('blue')) {
                    document.body.style.background = 'linear-gradient(135deg, #60a5fa, #22d3ee, #34d399)';
                } else if (themeGradient.includes('purple')) {
                    document.body.style.background = 'linear-gradient(135deg, #8b5cf6, #6366f1, #3b82f6)';
                } else if (themeGradient.includes('pink')) {
                    document.body.style.background = 'linear-gradient(135deg, #f472b6, #fb7185, #f87171)';
                } else if (themeGradient.includes('green')) {
                    document.body.style.background = 'linear-gradient(135deg, #4ade80, #34d399, #2dd4bf)';
                } else if (themeGradient.includes('gold')) {
                    document.body.style.background = 'linear-gradient(135deg, #facc15, #fbbf24, #fb923c)';
                } else if (themeGradient.includes('rainbow')) {
                    document.body.style.background = 'linear-gradient(135deg, #f472b6, #c084fc, #818cf8, #60a5fa, #4ade80, #facc15)';
                }
            }
        });
}

       function resetStats() {
           fetch('/reset_stats', { method: 'POST' })
               .then(response => response.json())
               .then(data => {
                   if (data.success) {
                       location.reload();
                   }
               });
       }

       function updateConfig() {
           const formData = new FormData();
           formData.append('language', document.getElementById('language').value);
           formData.append('mode', document.getElementById('mode').value);
           formData.append('syllable_count', document.getElementById('syllable_count').value);

           fetch('/update_config', { method: 'POST', body: formData })
               .then(response => response.json())
               .then(data => {
                   if (data.success) {
                       location.reload();
                   }
               });
       }

       function updateTimerButton() {
           const btn = document.getElementById('timer-btn');
           const icon = document.getElementById('timer-icon');
           const text = document.getElementById('timer-text');
           
           if (isPlaying) {
               btn.className = btn.className.replace('bg-green-500 hover:bg-green-600', 'bg-red-500 hover:bg-red-600');
               icon.textContent = '⏸️';
               text.textContent = 'Pausar';
           } else {
               btn.className = btn.className.replace('bg-red-500 hover:bg-red-600', 'bg-green-500 hover:bg-green-600');
               icon.textContent = '▶️';
               text.textContent = 'Iniciar';
           }
       }

       // Detectar barra espaciadora para siguiente elemento
       document.addEventListener('keydown', function(event) {
           if (event.code === 'Space' || event.key === ' ') {
               event.preventDefault(); // Evitar scroll de página
               nextItem();
           }
       });

       if (isPlaying && startTime) {
           setInterval(() => {
               const currentTime = Date.now() / 1000;
               const sessionTime = currentTime - startTime;
               const displayTime = totalTime + sessionTime;
               const minutes = Math.floor(displayTime / 60);
               const seconds = Math.floor(displayTime % 60);
               document.getElementById('time-display').textContent = 
                   minutes + ':' + seconds.toString().padStart(2, '0');
           }, 1000);
       }
   
   // Forzar cambio de fondo después de cargar
   document.addEventListener('DOMContentLoaded', function() {
       const themeGradient = '{{ theme_gradient }}';
       document.body.style.background = 'linear-gradient(135deg, #8b5cf6, #ec4899, #3b82f6)';
       document.body.style.backgroundAttachment = 'fixed';
       
       // Si hay tema específico, aplicarlo
       if (themeGradient.includes('yellow')) {
           document.body.style.background = 'linear-gradient(135deg, #fde68a, #fed7aa, #f87171)';
       } else if (themeGradient.includes('blue')) {
           document.body.style.background = 'linear-gradient(135deg, #60a5fa, #22d3ee, #34d399)';
       } else if (themeGradient.includes('purple')) {
           document.body.style.background = 'linear-gradient(135deg, #8b5cf6, #6366f1, #3b82f6)';
       } else if (themeGradient.includes('pink')) {
           document.body.style.background = 'linear-gradient(135deg, #f472b6, #fb7185, #f87171)';
       } else if (themeGradient.includes('green')) {
           document.body.style.background = 'linear-gradient(135deg, #4ade80, #34d399, #2dd4bf)';
       } else if (themeGradient.includes('gold')) {
           document.body.style.background = 'linear-gradient(135deg, #facc15, #fbbf24, #fb923c)';
       } else if (themeGradient.includes('rainbow')) {
           document.body.style.background = 'linear-gradient(135deg, #f472b6, #c084fc, #818cf8, #60a5fa, #4ade80, #facc15)';
       }
   });
</script>
</body>
</html>
'''

def init_session():
    if 'read_count' not in session:
        session['read_count'] = 0
        session['total_time'] = 0.0
        session['points'] = 0
        session['current_badge'] = None
        session['interface_theme'] = 'default'
        session['start_time'] = None
        session['is_playing'] = False
        session['mode'] = 'syllables'
        session['syllable_count'] = 1
        session['language'] = 'es'
        session['show_settings'] = False

def get_badge_styles(theme):
    styles = {
        'yellow': 'bg-gradient-to-r from-yellow-100 to-orange-100 shadow-lg border-2 border-yellow-400',
        'blue': 'bg-gradient-to-r from-blue-100 to-cyan-100 shadow-lg border-2 border-blue-400',
        'purple': 'bg-gradient-to-r from-purple-100 to-indigo-100 shadow-lg border-2 border-purple-400',
        'pink': 'bg-gradient-to-r from-pink-100 to-rose-100 shadow-lg border-2 border-pink-400',
        'green': 'bg-gradient-to-r from-green-100 to-emerald-100 shadow-lg border-2 border-green-400',
        'gold': 'bg-gradient-to-r from-yellow-100 to-orange-100 shadow-lg border-2 border-yellow-400',
        'rainbow': 'bg-gradient-to-r from-pink-100 via-purple-100 via-blue-100 to-green-100 shadow-lg border-2 border-pink-300'
    }
    return styles.get(theme, 'bg-gradient-to-r from-gray-100 to-gray-200')

@app.route('/')
def home():
    init_session()
    
    current_item = generar_item(session['mode'], session['syllable_count'], session['language'])
    pet_mood = get_pet_mood(session['read_count'])
    
    context = {
        'current_item': current_item,
        'read_count': session['read_count'],
        'total_time': session['total_time'],
        'points': session['points'],
        'level': (session['points'] // 100) + 1,
        'current_badge': session.get('current_badge'),
        'pet_emoji': get_pet_emoji(pet_mood),
        'pet_message': get_pet_message(pet_mood, session['language']),
        'theme_gradient': themes[session['interface_theme']],
        'time_formatted': f"{int(session['total_time'] // 60)}:{int(session['total_time'] % 60):02d}",
        'time_progress': min((session['total_time'] / 900) * 100, 100),
        'read_progress': min((session['read_count'] / 100) * 100, 100),
        'motivational_message': get_motivational_message(session['read_count'], session['language']) if session['read_count'] > 0 else None,
        'mode': session['mode'],
        'syllable_count': session['syllable_count'],
        'language': session['language'],
        'is_playing': session['is_playing'],
        'start_time': session.get('start_time'),
        'show_settings': session.get('show_settings', False),
        'new_badge': session.pop('new_badge', None),
        'get_badge_styles': get_badge_styles
    }
    
    return render_template_string(template, **context)

def get_motivational_message(read_count, language):
    messages = {
        'es': {
            'champion': '¡Eres una campeona de la lectura! 👑',
            'excellent': '¡Excelente progreso! ⚡',
            'good': '¡Vas muy bien! 🚀',
            'start': '¡Sigue leyendo! 📚'
        },
        'ca': {
            'champion': '¡Ets una campeona de la lectura! 👑',
            'excellent': '¡Excel·lent progrés! ⚡',
            'good': '¡Vas molt bé! 🚀',
            'start': '¡Continua llegint! 📚'
        }
    }
    
    lang_messages = messages.get(language, messages['es'])
    
    if read_count >= 100:
        return lang_messages['champion']
    elif read_count >= 60:
        return lang_messages['excellent']
    elif read_count >= 20:
        return lang_messages['good']
    else:
        return lang_messages['start']

@app.route('/next_item', methods=['POST'])
def next_item():
    current_time = time.time()
    
    if session.get('start_time'):
        session_time = current_time - session['start_time']
        session['total_time'] += session_time
        session['start_time'] = current_time
    else:
        session['start_time'] = current_time
    
    session['read_count'] += 1
    points_to_add = 2 if session['mode'] == 'syllables' else 5
    session['points'] += points_to_add
    
    new_badge = check_badges(
        session['read_count'],
        session['total_time'],
        session.get('current_badge'),
        session['language']
    )
    
    if new_badge:
        session['current_badge'] = new_badge
        session['interface_theme'] = new_badge['theme']
        session['new_badge'] = new_badge
    
    # Generar nuevo item
    new_item = generar_item(session['mode'], session['syllable_count'], session['language'])
    
    return jsonify({
        'success': True,
        'new_item': new_item,
        'theme_gradient': themes[session['interface_theme']],
        'read_count': session['read_count'],
        'points': session['points'],
        'level': (session['points'] // 100) + 1,
        'new_badge': new_badge
    })
@app.route('/toggle_timer', methods=['POST'])
def toggle_timer():
    current_time = time.time()
    
    if not session.get('is_playing'):
        session['start_time'] = current_time
        session['is_playing'] = True
    else:
        if session.get('start_time'):
            session['total_time'] += current_time - session['start_time']
        session['is_playing'] = False
        session['start_time'] = None
    
    return jsonify({
        'success': True,
        'is_playing': session['is_playing'],
        'start_time': session.get('start_time')
    })

@app.route('/reset_stats', methods=['POST'])
def reset_stats():
    session['read_count'] = 0
    session['total_time'] = 0.0
    session['points'] = 0
    session['current_badge'] = None
    session['interface_theme'] = 'default'
    session['start_time'] = None
    session['is_playing'] = False
    session.pop('new_badge', None)
    
    return jsonify({'success': True})

@app.route('/update_config', methods=['POST'])
def update_config():
    session['language'] = request.form.get('language', 'es')
    session['mode'] = request.form.get('mode', 'syllables')
    session['syllable_count'] = int(request.form.get('syllable_count', 1))
    
    return jsonify({'success': True})

if __name__ == '__main__':
    print("🏰 ¡LectoLandia COMPLETA se está iniciando!")
    print("📱 Interfaz idéntica a tu React original")
    print("🎮 Sistema completo de gamificación")
    print("⏱️ Cronómetro funcional")
    print("🏷️ Sistema de insignias")
    print("🌈 Temas dinámicos")
    print("📝 Ve a: http://localhost:5000")
    print("-" * 50)
    if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))