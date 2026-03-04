import streamlit as st
import streamlit.components.v1 as components

# ============== 核心数据 ==============

KEY_SCALES = {
    "C大调": [0, 2, 4, 5, 7, 9, 11],
    "G大调": [7, 9, 11, 0, 2, 4, 6],
    "D大调": [2, 4, 6, 7, 9, 11, 1],
    "A大调": [9, 11, 1, 2, 4, 6, 8],
    "E大调": [4, 6, 8, 9, 11, 1, 3],
    "B大调": [11, 1, 3, 4, 6, 8, 10],
    "Gb大调": [6, 8, 10, 11, 1, 3, 5],
    "Db大调": [1, 3, 5, 6, 8, 10, 0],
    "Ab大调": [8, 10, 0, 1, 3, 5, 7],
    "Eb大调": [3, 5, 7, 8, 10, 0, 2],
    "Bb大调": [10, 0, 2, 3, 5, 7, 9],
    "F大调": [5, 7, 9, 10, 0, 2, 4]
}

NOTE_NAMES = ["C", "C#\nDb", "D", "D#\nEb", "E", "F", "F#\nGb", "G", "G#\nAb", "A", "A#\nBb", "B"]

KEY_NOTE_NAMES = {
    "C大调": ["C", "D", "E", "F", "G", "A", "B"],
    "G大调": ["G", "A", "B", "C", "D", "E", "F#"],
    "D大调": ["D", "E", "F#", "G", "A", "B", "C#"],
    "A大调": ["A", "B", "C#", "D", "E", "F#", "G#"],
    "E大调": ["E", "F#", "G#", "A", "B", "C#", "D#"],
    "B大调": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
    "Gb大调": ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"],
    "Db大调": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"],
    "Ab大调": ["Ab", "Bb", "C", "Db", "Eb", "F", "G"],
    "Eb大调": ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
    "Bb大调": ["Bb", "C", "D", "Eb", "F", "G", "A"],
    "F大调": ["F", "G", "A", "Bb", "C", "D", "E"],
}

RIGHT_FINGERINGS = {
    "C大调": [1, 2, 3, 1, 2, 3, 4, 5],
    "G大调": [1, 2, 3, 1, 2, 3, 4, 5],
    "D大调": [1, 2, 3, 1, 2, 3, 4, 5],
    "A大调": [1, 2, 3, 1, 2, 3, 4, 5],
    "E大调": [1, 2, 3, 1, 2, 3, 4, 5],
    "B大调": [1, 2, 3, 1, 2, 3, 4, 5],
    "Bb大调": [2, 1, 2, 3, 1, 2, 3, 4],
    "Eb大调": [3, 1, 2, 3, 4, 1, 2, 3],
    "Ab大调": [3, 4, 1, 2, 3, 1, 2, 3],
    "Gb大调": [2, 3, 4, 1, 2, 3, 1, 2],
    "Db大调": [2, 3, 1, 2, 3, 4, 1, 2],
    "F大调": [1, 2, 3, 4, 1, 2, 3, 4],
}

LEFT_FINGERINGS = {
    "C大调": [5, 4, 3, 5, 4, 3, 2, 1],
    "G大调": [5, 4, 3, 5, 4, 3, 2, 1],
    "D大调": [5, 4, 3, 5, 4, 3, 2, 1],
    "A大调": [5, 4, 3, 5, 4, 3, 2, 1],
    "E大调": [5, 4, 3, 5, 4, 3, 2, 1],
    "B大调": [5, 4, 3, 5, 4, 3, 2, 1],
    "Bb大调": [4, 5, 4, 3, 5, 4, 3, 2],
    "Eb大调": [3, 5, 4, 3, 2, 5, 4, 3],
    "Ab大调": [3, 2, 5, 4, 3, 5, 4, 3],
    "Gb大调": [4, 3, 2, 5, 4, 3, 5, 4],
    "Db大调": [4, 3, 5, 4, 3, 2, 5, 4],
    "F大调": [5, 4, 3, 2, 5, 4, 3, 2],
}

NOTE_TO_KEY = {
    0: "C大调", 1: "Db大调", 2: "D大调", 3: "Eb大调",
    4: "E大调", 5: "F大调", 6: "Gb大调", 7: "G大调",
    8: "Ab大调", 9: "A大调", 10: "Bb大调", 11: "B大调"
}

KEY_LETTER_TO_FULL = {
    "C": "C大调", "Db": "Db大调", "D": "D大调", "Eb": "Eb大调",
    "E": "E大调", "F": "F大调", "Gb": "Gb大调", "G": "G大调",
    "Ab": "Ab大调", "A": "A大调", "Bb": "Bb大调", "B": "B大调"
}


def get_note_position(actual_note, start_x, start_y, white_key_width):
    white_keys_pattern = [0, 2, 4, 5, 7, 9, 11]
    black_keys_pattern = [1, 3, 6, 8, 10]
    black_key_offsets = [0.5, 1.5, 3.5, 4.5, 5.5]
    
    octave = actual_note // 12
    note_in_octave = actual_note % 12
    
    if note_in_octave in white_keys_pattern:
        idx = white_keys_pattern.index(note_in_octave)
        x = start_x + (octave * 7 + idx) * white_key_width + white_key_width // 2
        return (x, "white")
    elif note_in_octave in black_keys_pattern:
        idx = black_keys_pattern.index(note_in_octave)
        x = start_x + (octave * 7 + black_key_offsets[idx]) * white_key_width + 12
        return (x, "black")
    return None


def draw_piano_svg(selected_key, hand_mode, is_mobile=False):
    # 移动端使用更小的尺寸
    if is_mobile:
        canvas_width = 360
        canvas_height = 220  # 增加高度容纳启用按钮
        white_key_width = 20
        white_key_height = 100
        black_key_width = 14
        black_key_height = 60
        font_size_white = 8
        font_size_black = 7
        font_size_finger_white = 10
        font_size_finger_black = 9
        circle_r_white = 6
        circle_r_black = 5
    else:
        canvas_width = 700
        canvas_height = 380
        white_key_width = 40
        white_key_height = 200
        black_key_width = 25
        black_key_height = 115
        font_size_white = 12
        font_size_black = 9
        font_size_finger_white = 14
        font_size_finger_black = 12
        circle_r_white = 10
        circle_r_black = 8
    
    keyboard_width = 14 * white_key_width
    start_x = (canvas_width - keyboard_width) // 2
    start_y = (canvas_height - white_key_height) // 2 - 30
    
    white_keys_pattern = [0, 2, 4, 5, 7, 9, 11]
    black_keys_pattern = [1, 3, 6, 8, 10]
    black_key_offsets = [0.5, 1.5, 3.5, 4.5, 5.5]
    
    # 音符频率映射表（C4-B5）
    note_frequencies = {
        # 第一个八度 (C4-B4)
        0: 261.63,   # C4
        1: 277.18,   # C#4/Db4
        2: 293.66,   # D4
        3: 311.13,   # D#4/Eb4
        4: 329.63,   # E4
        5: 349.23,   # F4
        6: 369.99,   # F#4/Gb4
        7: 392.00,   # G4
        8: 415.30,   # G#4/Ab4
        9: 440.00,   # A4
        10: 466.16,  # A#4/Bb4
        11: 493.88,  # B4
        # 第二个八度 (C5-B5)
        12: 523.25,  # C5
        13: 554.37,  # C#5/Db5
        14: 587.33,  # D5
        15: 622.25,  # D#5/Eb5
        16: 659.25,  # E5
        17: 698.46,  # F5
        18: 739.99,  # F#5/Gb5
        19: 783.99,  # G5
        20: 830.61,  # G#5/Ab5
        21: 880.00,  # A5
        22: 932.33,  # A#5/Bb5
        23: 987.77,  # B5
    }
    
    svg_elements = []
    
    # 绘制白键（两个八度）- 添加class和data属性用于交互
    for octave in range(2):
        for i, note_num in enumerate(white_keys_pattern):
            x = start_x + (octave * 7 + i) * white_key_width
            actual_note = note_num + octave * 12
            freq = note_frequencies.get(actual_note, 440)
            note_name_display = NOTE_NAMES[note_num].replace('\n', '/')
            
            svg_elements.append(f'<rect class="piano-key white-key" data-note="{actual_note}" data-freq="{freq}" x="{x}" y="{start_y}" width="{white_key_width}" height="{white_key_height}" fill="white" stroke="black" stroke-width="1" style="cursor: pointer;"/>')
            text_y = start_y + white_key_height - (8 if is_mobile else 15)
            svg_elements.append(f'<text x="{x + white_key_width//2}" y="{text_y}" font-size="{font_size_white}" text-anchor="middle" fill="black" pointer-events="none">{note_name_display}</text>')
    
    # 绘制八度分隔线
    mid_x = start_x + 7 * white_key_width
    svg_elements.append(f'<line x1="{mid_x}" y1="{start_y - 5}" x2="{mid_x}" y2="{start_y + white_key_height + 5}" stroke="red" stroke-width="2" stroke-dasharray="5,3"/>')
    
    # 绘制黑键（两个八度）- 添加class和data属性用于交互
    for octave in range(2):
        for i, note_num in enumerate(black_keys_pattern):
            x = start_x + (octave * 7 + black_key_offsets[i]) * white_key_width
            actual_note = note_num + octave * 12
            freq = note_frequencies.get(actual_note, 440)
            
            svg_elements.append(f'<rect class="piano-key black-key" data-note="{actual_note}" data-freq="{freq}" x="{x}" y="{start_y}" width="{black_key_width}" height="{black_key_height}" fill="black" stroke="black" stroke-width="1" style="cursor: pointer;"/>')
            note_name = NOTE_NAMES[note_num]
            if '\n' in note_name:
                sharp, flat = note_name.split('\n')
                text_y1 = start_y + black_key_height - (18 if is_mobile else 30)
                text_y2 = start_y + black_key_height - (8 if is_mobile else 15)
                svg_elements.append(f'<text x="{x + black_key_width//2}" y="{text_y1}" font-size="{font_size_black}" fill="cyan" text-anchor="middle" pointer-events="none">{sharp}</text>')
                svg_elements.append(f'<text x="{x + black_key_width//2}" y="{text_y2}" font-size="{font_size_black}" fill="cyan" text-anchor="middle" pointer-events="none">{flat}</text>')
    
    # 高亮显示当前调式的音阶
    base_scale_notes = KEY_SCALES[selected_key]
    start_note = base_scale_notes[0]
    octave_start = 0
    
    major_scale_intervals = [0, 2, 4, 5, 7, 9, 11]
    scale_notes = [start_note + interval + octave_start * 12 for interval in major_scale_intervals]
    
    fingering = RIGHT_FINGERINGS[selected_key] if hand_mode == "右手" else LEFT_FINGERINGS[selected_key]
    
    for i, actual_note in enumerate(scale_notes):
        pos = get_note_position(actual_note, start_x, start_y, white_key_width)
        if pos:
            x, key_type = pos
            finger_num = fingering[i]
            
            if key_type == "white":
                y_white = start_y + white_key_height - 35 if is_mobile else start_y + 155
                svg_elements.append(f'<circle cx="{x}" cy="{y_white}" r="{circle_r_white}" fill="yellow" stroke="orange" stroke-width="1" pointer-events="none"/>')
                text_y = y_white - (12 if is_mobile else 20)
                svg_elements.append(f'<text x="{x}" y="{text_y}" font-size="{font_size_finger_white}" font-weight="bold" fill="red" text-anchor="middle" pointer-events="none">{finger_num}</text>')
            else:
                y_black = start_y + black_key_height - 20 if is_mobile else start_y + black_key_height - 35
                svg_elements.append(f'<circle cx="{x}" cy="{y_black}" r="{circle_r_black}" fill="yellow" stroke="orange" stroke-width="1" pointer-events="none"/>')
                text_y = y_black - (10 if is_mobile else 18)
                svg_elements.append(f'<text x="{x}" y="{text_y}" font-size="{font_size_finger_black}" font-weight="bold" fill="red" text-anchor="middle" pointer-events="none">{finger_num}</text>')
    
    svg_content = '\n'.join(svg_elements)
    
    # JavaScript 用于音频播放和交互
    js_code = '''
    <script>
    (function() {
        let audioContext = null;
        let activeOscillators = {};
        
        // 初始化音频上下文
        function initAudio() {
            if (!audioContext) {
                audioContext = new (window.AudioContext || window.webkitAudioContext)();
            }
            if (audioContext.state === 'suspended') {
                audioContext.resume();
            }
        }
        
        // 播放音符
        function playNote(noteId, frequency) {
            initAudio();
            
            // 如果该音符已经在播放，先停止
            if (activeOscillators[noteId]) {
                stopNote(noteId);
            }
            
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();
            
            // 使用三角波，更接近钢琴音色
            oscillator.type = 'triangle';
            oscillator.frequency.value = parseFloat(frequency);
            
            // 设置音量包络
            gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
            gainNode.gain.exponentialRampToValueAtTime(0.1, audioContext.currentTime + 0.3);
            
            oscillator.connect(gainNode);
            gainNode.connect(audioContext.destination);
            
            oscillator.start();
            
            activeOscillators[noteId] = { oscillator, gainNode };
            
            // 视觉反馈
            const key = document.querySelector(`[data-note="${noteId}"]`);
            if (key) {
                if (key.classList.contains('white-key')) {
                    key.setAttribute('fill', '#e0e0e0');
                } else {
                    key.setAttribute('fill', '#333333');
                }
            }
        }
        
        // 停止音符
        function stopNote(noteId) {
            if (activeOscillators[noteId]) {
                const { oscillator, gainNode } = activeOscillators[noteId];
                
                // 淡出
                gainNode.gain.cancelScheduledValues(audioContext.currentTime);
                gainNode.gain.setValueAtTime(gainNode.gain.value, audioContext.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.1);
                
                oscillator.stop(audioContext.currentTime + 0.15);
                
                delete activeOscillators[noteId];
                
                // 恢复视觉
                const key = document.querySelector(`[data-note="${noteId}"]`);
                if (key) {
                    if (key.classList.contains('white-key')) {
                        key.setAttribute('fill', 'white');
                    } else {
                        key.setAttribute('fill', 'black');
                    }
                }
            }
        }
        
        // 为所有琴键添加事件监听
        const keys = document.querySelectorAll('.piano-key');
        keys.forEach(key => {
            const noteId = key.getAttribute('data-note');
            const frequency = key.getAttribute('data-freq');
            
            // 鼠标事件
            key.addEventListener('mousedown', function(e) {
                e.preventDefault();
                playNote(noteId, frequency);
            });
            
            key.addEventListener('mouseup', function() {
                stopNote(noteId);
            });
            
            key.addEventListener('mouseleave', function() {
                stopNote(noteId);
            });
            
            // 触摸事件（移动端）
            key.addEventListener('touchstart', function(e) {
                e.preventDefault();
                playNote(noteId, frequency);
            });
            
            key.addEventListener('touchend', function(e) {
                e.preventDefault();
                stopNote(noteId);
            });
        });
        
        // 防止触摸时页面滚动
        document.addEventListener('touchmove', function(e) {
            if (e.target.classList.contains('piano-key')) {
                e.preventDefault();
            }
        }, { passive: false });
    })();
    </script>
    '''
    
    html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <style>
        body {{ 
            margin: 0; 
            padding: 0; 
            display: flex; 
            flex-direction: column;
            justify-content: center; 
            align-items: center; 
            background-color: white; 
            font-family: Arial, sans-serif;
        }}
        svg {{ display: block; }}
        .piano-key {{
            transition: fill 0.05s ease;
        }}
        .white-key:active {{
            fill: #d0d0d0 !important;
        }}
        .black-key:active {{
            fill: #444444 !important;
        }}
    </style>
</head>
<body>
    <svg width="{canvas_width}" height="{canvas_height - 60}" viewBox="0 0 {canvas_width} {canvas_height - 60}" xmlns="http://www.w3.org/2000/svg">
        <rect width="100%" height="100%" fill="white" stroke="#cccccc" stroke-width="0"/>
        {svg_content}
    </svg>
    {js_code}
</body>
</html>'''
    
    return html


def draw_piano_svg_vertical(selected_key, hand_mode):
    """绘制竖直显示的钢琴键盘（适合移动端竖屏）
    注意：C在底部，从下往上是 C-D-E-F-G-A-B，这样横屏时从左到右是正常的顺序
    """
    canvas_width = 360
    canvas_height = 900  # 画布增大
    
    # 放大比例因子（所有尺寸按此比例放大，保持相对比例不变）
    scale = 1.2
    
    white_key_height = int(35 * scale)   # 42
    white_key_width = int(180 * scale)   # 216
    black_key_height = int(22 * scale)   # 26
    black_key_width = int(90 * scale)    # 108
    
    # 键盘在画布中上下居中
    keyboard_height = 14 * white_key_height
    start_y = (canvas_height + keyboard_height) // 2 - 120
    start_x = (canvas_width - white_key_width) // 2
    
    # 白键音高（从下往上：C-D-E-F-G-A-B）
    white_keys_pattern = [0, 2, 4, 5, 7, 9, 11]  # C-D-E-F-G-A-B
    # 黑键音高
    black_keys_pattern = [1, 3, 6, 8, 10]  # Db-Eb-Gb-Ab-Bb
    # 黑键在白键之间的偏移（从下往上）
    black_key_offsets = [0.5, 1.5, 3.5, 4.5, 5.5]
    
    # 音符频率映射表（C4-B5）
    note_frequencies = {
        0: 261.63, 1: 277.18, 2: 293.66, 3: 311.13,
        4: 329.63, 5: 349.23, 6: 369.99, 7: 392.00,
        8: 415.30, 9: 440.00, 10: 466.16, 11: 493.88,
        12: 523.25, 13: 554.37, 14: 587.33, 15: 622.25,
        16: 659.25, 17: 698.46, 18: 739.99, 19: 783.99,
        20: 830.61, 21: 880.00, 22: 932.33, 23: 987.77,
    }
    
    svg_elements = []
    
    # 绘制白键（从下往上绘制，C在底部）- 添加class和data属性
    for octave in range(2):
        for i, note_num in enumerate(white_keys_pattern):
            # 从底部向上计算y坐标
            y = start_y - ((octave * 7 + i + 1) * white_key_height)
            actual_note = note_num + octave * 12
            freq = note_frequencies.get(actual_note, 440)
            note_name_display = NOTE_NAMES[note_num].replace('\n', '/')
            
            svg_elements.append(f'<rect class="piano-key-v white-key-v" data-note="{actual_note}" data-freq="{freq}" x="{start_x}" y="{y}" width="{white_key_width}" height="{white_key_height}" fill="white" stroke="black" stroke-width="1" style="cursor: pointer;"/>')
            text_x = start_x + white_key_width - 15
            text_y = y + white_key_height // 2
            svg_elements.append(f'<text x="{text_x}" y="{text_y}" font-size="19" text-anchor="middle" fill="black" transform="rotate(-90, {text_x}, {text_y})" pointer-events="none">{note_name_display}</text>')
    
    # 绘制八度分隔线（在第7个白键和第8个白键之间）
    mid_y = start_y - (7 * white_key_height)
    svg_elements.append(f'<line x1="{start_x - 5}" y1="{mid_y}" x2="{start_x + white_key_width + 5}" y2="{mid_y}" stroke="red" stroke-width="2" stroke-dasharray="5,3"/>')
    
    # 绘制黑键（从下往上绘制）- 添加class和data属性
    black_key_x = start_x  # 黑键靠左对齐
    for octave in range(2):
        for i, note_num in enumerate(black_keys_pattern):
            # 黑键位置基于白键位置计算
            y = start_y - ((octave * 7 + black_key_offsets[i] + 0.5) * white_key_height) - black_key_height//2
            actual_note = note_num + octave * 12
            freq = note_frequencies.get(actual_note, 440)
            
            svg_elements.append(f'<rect class="piano-key-v black-key-v" data-note="{actual_note}" data-freq="{freq}" x="{black_key_x}" y="{y}" width="{black_key_width}" height="{black_key_height}" fill="black" stroke="black" stroke-width="1" style="cursor: pointer;"/>')
            note_name = NOTE_NAMES[note_num]
            if '\n' in note_name:
                sharp, flat = note_name.split('\n')
                text_x = black_key_x + 32
                text_y = y + black_key_height // 2
                svg_elements.append(f'<text x="{text_x}" y="{text_y}" font-size="13" fill="cyan" text-anchor="middle" transform="rotate(-90, {text_x}, {text_y})" pointer-events="none">{sharp}</text>')
    
    # 高亮显示当前调式的音阶
    base_scale_notes = KEY_SCALES[selected_key]
    start_note = base_scale_notes[0]
    octave_start = 0
    
    major_scale_intervals = [0, 2, 4, 5, 7, 9, 11]
    scale_notes = [start_note + interval + octave_start * 12 for interval in major_scale_intervals]
    
    fingering = RIGHT_FINGERINGS[selected_key] if hand_mode == "右手" else LEFT_FINGERINGS[selected_key]
    
    for i, actual_note in enumerate(scale_notes):
        octave = actual_note // 12
        note_in_octave = actual_note % 12
        
        if note_in_octave in white_keys_pattern:
            idx = white_keys_pattern.index(note_in_octave)
            # 从底部向上计算y坐标（琴键中心）
            key_center_y = start_y - ((octave * 7 + idx) * white_key_height) - white_key_height // 2
            
            # 标记放在白键上（横屏时黄点在右，数字在上）
            mark_x = start_x + white_key_width - 45  # 黄点位置
            dot_y = key_center_y
            # 数字在黄点左边（横屏时就是上方）
            num_x = mark_x - 16
            num_y = dot_y
            
            # 先画黄点，再画数字
            svg_elements.append(f'<circle cx="{mark_x}" cy="{dot_y}" r="10" fill="yellow" stroke="orange" stroke-width="1" pointer-events="none"/>')
            svg_elements.append(f'<text x="{num_x}" y="{num_y}" font-size="16" font-weight="bold" fill="red" text-anchor="middle" transform="rotate(-90, {num_x}, {num_y})" pointer-events="none">{fingering[i]}</text>')
            
        elif note_in_octave in black_keys_pattern:
            idx = black_keys_pattern.index(note_in_octave)
            # 黑键中心y坐标（必须与绘制时的计算一致）
            key_center_y = start_y - ((octave * 7 + black_key_offsets[idx] + 0.5) * white_key_height)
            
            # 黄点位置（横屏时左右居中 = 竖直画布y方向上下居中）
            dot_x = start_x + black_key_width - 20
            dot_y = key_center_y
            
            # 红字位置（在黄点左边/上方，横屏时在黄点和蓝字母之间）
            num_x = dot_x - 14
            num_y = key_center_y
            
            # 先画黄点（最下），再画红字
            svg_elements.append(f'<circle cx="{dot_x}" cy="{dot_y}" r="7" fill="yellow" stroke="orange" stroke-width="1" pointer-events="none"/>')
            svg_elements.append(f'<text x="{num_x}" y="{num_y}" font-size="13" font-weight="bold" fill="red" text-anchor="middle" transform="rotate(-90, {num_x}, {num_y})" pointer-events="none">{fingering[i]}</text>')
    
    svg_content = '\n'.join(svg_elements)
    
    # JavaScript 用于音频播放和交互（竖直布局）
    js_code = '''
    <script>
    (function() {
        let audioContext = null;
        let activeOscillators = {};
        
        function initAudio() {
            if (!audioContext) {
                audioContext = new (window.AudioContext || window.webkitAudioContext)();
            }
            if (audioContext.state === 'suspended') {
                audioContext.resume();
            }
        }
        
        function playNote(noteId, frequency) {
            initAudio();
            
            if (activeOscillators[noteId]) {
                stopNote(noteId);
            }
            
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();
            
            oscillator.type = 'triangle';
            oscillator.frequency.value = parseFloat(frequency);
            
            gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
            gainNode.gain.exponentialRampToValueAtTime(0.1, audioContext.currentTime + 0.3);
            
            oscillator.connect(gainNode);
            gainNode.connect(audioContext.destination);
            
            oscillator.start();
            
            activeOscillators[noteId] = { oscillator, gainNode };
            
            // 视觉反馈
            const key = document.querySelector(`[data-note="${noteId}"]`);
            if (key) {
                if (key.classList.contains('white-key-v')) {
                    key.setAttribute('fill', '#e0e0e0');
                } else {
                    key.setAttribute('fill', '#333333');
                }
            }
        }
        
        function stopNote(noteId) {
            if (activeOscillators[noteId]) {
                const { oscillator, gainNode } = activeOscillators[noteId];
                
                gainNode.gain.cancelScheduledValues(audioContext.currentTime);
                gainNode.gain.setValueAtTime(gainNode.gain.value, audioContext.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.1);
                
                oscillator.stop(audioContext.currentTime + 0.15);
                
                delete activeOscillators[noteId];
                
                // 恢复视觉
                const key = document.querySelector(`[data-note="${noteId}"]`);
                if (key) {
                    if (key.classList.contains('white-key-v')) {
                        key.setAttribute('fill', 'white');
                    } else {
                        key.setAttribute('fill', 'black');
                    }
                }
            }
        }
        
        // 为所有琴键添加事件监听
        const keys = document.querySelectorAll('.piano-key-v');
        keys.forEach(key => {
            const noteId = key.getAttribute('data-note');
            const frequency = key.getAttribute('data-freq');
            
            // 鼠标事件
            key.addEventListener('mousedown', function(e) {
                e.preventDefault();
                playNote(noteId, frequency);
            });
            
            key.addEventListener('mouseup', function() {
                stopNote(noteId);
            });
            
            key.addEventListener('mouseleave', function() {
                stopNote(noteId);
            });
            
            // 触摸事件
            key.addEventListener('touchstart', function(e) {
                e.preventDefault();
                playNote(noteId, frequency);
            });
            
            key.addEventListener('touchend', function(e) {
                e.preventDefault();
                stopNote(noteId);
            });
        });
        
        // 防止触摸时页面滚动
        document.addEventListener('touchmove', function(e) {
            if (e.target.classList.contains('piano-key-v')) {
                e.preventDefault();
            }
        }, { passive: false });
    })();
    </script>
    '''
    
    html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <style>
        body {{ 
            margin: 0; 
            padding: 0; 
            display: flex; 
            flex-direction: column;
            justify-content: center; 
            align-items: center; 
            background-color: white; 
            min-height: 100vh;
            font-family: Arial, sans-serif;
        }}
        svg {{ display: block; }}
        .piano-key-v {{
            transition: fill 0.05s ease;
        }}
        .white-key-v:active {{
            fill: #d0d0d0 !important;
        }}
        .black-key-v:active {{
            fill: #444444 !important;
        }}
    </style>
</head>
<body>
    <svg width="{canvas_width}" height="{canvas_height - 60}" viewBox="0 0 {canvas_width} {canvas_height - 60}" xmlns="http://www.w3.org/2000/svg">
        <rect width="100%" height="100%" fill="white" stroke="white" stroke-width="2"/>
        {svg_content}
    </svg>
    {js_code}
</body>
</html>'''
    
    return html


def main():
    # 检测是否为移动端（通过URL参数或屏幕宽度检测）
    is_mobile = st.query_params.get('mobile', 'false').lower() == 'true'
    
    # 如果没有明确指定，使用JavaScript自动检测屏幕宽度
    if not is_mobile and 'mobile' not in st.query_params:
        st.markdown("""
        <script>
        // 自动检测屏幕宽度，如果是移动端则自动切换
        if (window.innerWidth <= 768) {
            // 添加 mobile=true 参数并刷新页面
            const url = new URL(window.location.href);
            url.searchParams.set('mobile', 'true');
            window.location.href = url.toString();
        }
        </script>
        """, unsafe_allow_html=True)
    
    st.set_page_config(page_title="12个大调钢琴指法演示", layout="wide")
    
    # 桌面端显示标题，移动端不显示
    if not is_mobile:
        st.markdown("<h2 style='margin-top: -1rem; margin-bottom: 1rem;'>🎹 12个大调钢琴指法演示</h2>", unsafe_allow_html=True)
    
    # 初始化 session state
    if "key" not in st.session_state:
        st.session_state.key = "C大调"
    if "hand" not in st.session_state:
        st.session_state.hand = "右手"
    
    if is_mobile:
        # === 移动端布局 ===
        # 添加标题
        st.markdown("<h3 style='text-align: center; margin-top: 3rem; margin-bottom: 0.2rem;'>🎹 12个大调钢琴指法演示</h3>", unsafe_allow_html=True)
        
        st.markdown("""
        <style>
        .block-container { padding-top: 0; padding-bottom: 0; }
        div[data-testid="stVerticalBlock"] > div { margin-bottom: 0rem; }
        .stRadio > div { flex-direction: row; gap: 1rem; justify-content: center; }
        .stRadio label { margin-bottom: 0; }
        </style>
        """, unsafe_allow_html=True)
        
        # 第一行：先处理调式选择逻辑（在渲染键盘之前）
        # 检查URL参数是否有调式更新
        query_params = st.query_params
        if "key" in query_params:
            key_map = {
                "C": "C大调", "Db": "Db大调", "D": "D大调", "Eb": "Eb大调",
                "E": "E大调", "F": "F大调", "Gb": "Gb大调", "G": "G大调",
                "Ab": "Ab大调", "A": "A大调", "Bb": "Bb大调", "B": "B大调"
            }
            key_val = query_params["key"]
            if key_val in key_map:
                new_key = key_map[key_val]
                if new_key != st.session_state.key:
                    st.session_state.key = new_key
                    # 清除参数避免重复处理
                    del st.query_params["key"]
                    st.rerun()
        
        # 第二行：竖直显示的钢琴键盘（使用更新后的调式）
        svg_html = draw_piano_svg_vertical(st.session_state.key, st.session_state.hand)
        components.html(svg_html, height=650, scrolling=False)
        
        # 第三行：调式选择（使用Streamlit原生selectbox）
        key_options = ["C大调", "D大调", "E大调", "F大调", "G大调", "A大调", "B大调",
                       "Db大调", "Eb大调", "Gb大调", "Ab大调", "Bb大调"]
        
        selected_key = st.selectbox(
            "选择调式", 
            key_options,
            index=key_options.index(st.session_state.key),
            label_visibility="collapsed",
            key="mobile_key_selector"
        )
        
        # 如果调式改变，更新并刷新
        if selected_key != st.session_state.key:
            st.session_state.key = selected_key
            st.rerun()
        
        # 第三行：音阶和指法信息
        scale_names = KEY_NOTE_NAMES[st.session_state.key]
        fingering = RIGHT_FINGERINGS[st.session_state.key] if st.session_state.hand == "右手" else LEFT_FINGERINGS[st.session_state.key]
        
        info_col1, info_col2 = st.columns(2)
        with info_col1:
            st.info(f"**音阶**：{' '.join(scale_names)}")
        with info_col2:
            st.info(f"**指法**：{' '.join(map(str, fingering))}")
        
        # 第四行：左右手切换
        hand_mode = st.radio("hand_selection", ["右手", "左手"], 
                            index=0 if st.session_state.hand == "右手" else 1,
                            horizontal=True, label_visibility="collapsed")
        st.session_state.hand = hand_mode
        
        # 展开区：指法分组参考表
        with st.expander("📋 指法分组参考", expanded=False):
            st.markdown("""<style>
            table.fingering-table { width: 100% !important; border-collapse: collapse; table-layout: fixed; font-size: 0.8rem; }
            table.fingering-table tr { height: 1.6em !important; }
            table.fingering-table td, table.fingering-table th { padding: 2px 4px !important; line-height: 1.4 !important; text-align: center !important; border: 1px solid #ddd; }
            table.fingering-table th { background-color: white; font-weight: bold; }
            table.fingering-table td:first-child { font-weight: bold; background-color: #fafafa; }
            .group-header { background-color: #e8e8e8 !important; font-weight: bold; color: #666; font-size: 0.75rem !important; }
            </style>""", unsafe_allow_html=True)
            
            st.markdown("""<table class="fingering-table">
            <tr><th>调</th><th>右手</th><th>左手</th></tr>
            <tr><td class="group-header" colspan="3">基本组（第3指后穿拇指）</td></tr>
            <tr><td>C</td><td>12312345</td><td>54354321</td></tr>
            <tr><td>G</td><td>12312345</td><td>54354321</td></tr>
            <tr><td>D</td><td>12312345</td><td>54354321</td></tr>
            <tr><td>A</td><td>12312345</td><td>54354321</td></tr>
            <tr><td>E</td><td>12312345</td><td>54354321</td></tr>
            <tr><td class="group-header" colspan="3">黑键起步组（拇指不弹黑键）</td></tr>
            <tr><td>Bb</td><td>21231234</td><td>45435432</td></tr>
            <tr><td>Eb</td><td>31234123</td><td>35432543</td></tr>
            <tr><td>Ab</td><td>34123123</td><td>32543543</td></tr>
            <tr><td class="group-header" colspan="3">特殊组（长手指弹黑键，B大调注意穿指）</td></tr>
            <tr><td>B</td><td>12312345</td><td>54354321</td></tr>
            <tr><td>Gb</td><td>23412312</td><td>43254354</td></tr>
            <tr><td>Db</td><td>23123412</td><td>43543254</td></tr>
            <tr><td class="group-header" colspan="3">F大调例外（第4指后穿拇指）</td></tr>
            <tr><td>F</td><td>12341234</td><td>54325432</td></tr>
            </table>""", unsafe_allow_html=True)
    else:
        # === 桌面端布局 ===
        col1, col2, col3 = st.columns([1.2, 2.5, 1.3])
        
        with col1:
            st.subheader("左右手")
            hand_mode = st.radio("hand_selection", ["右手", "左手"], label_visibility="collapsed", 
                                index=0 if st.session_state.hand == "右手" else 1,
                                horizontal=True)
            st.session_state.hand = hand_mode
            
            st.divider()
            st.subheader("手指说明")
            if st.session_state.hand == "右手":
                st.markdown("- **1** = 拇指\n- **2** = 食指  \n- **3** = 中指\n- **4** = 无名指\n- **5** = 小指")
            else:
                st.markdown("- **1** = 小指\n- **2** = 无名指\n- **3** = 中指\n- **4** = 食指\n- **5** = 拇指")
        
        with col2:
            # 调式选择下拉菜单 - 使用较窄的列
            key_sel_col, _ = st.columns([1, 3])
            with key_sel_col:
                key_options = ["C大调", "D大调", "E大调", "F大调", "G大调", "A大调", "B大调",
                               "Db大调", "Eb大调", "Gb大调", "Ab大调", "Bb大调"]
                selected_key = st.selectbox("选择调式", key_options, 
                                            index=key_options.index(st.session_state.key),
                                            label_visibility="collapsed")
                # 如果调式改变，更新并刷新
                if selected_key != st.session_state.key:
                    st.session_state.key = selected_key
                    st.rerun()
            
            svg_html = draw_piano_svg(st.session_state.key, st.session_state.hand, is_mobile=False)
            components.html(svg_html, height=320, scrolling=False)
            
            scale_names = KEY_NOTE_NAMES[st.session_state.key]
            fingering = RIGHT_FINGERINGS[st.session_state.key] if st.session_state.hand == "右手" else LEFT_FINGERINGS[st.session_state.key]
            
            info_col1, info_col2 = st.columns(2)
            with info_col1:
                st.info(f"**音阶**：{'    '.join(scale_names)}")
            with info_col2:
                st.info(f"**{st.session_state.hand}指法**：{'    '.join(map(str, fingering))}")
        
        with col3:
            st.subheader("指法分组参考")
            
            st.markdown("""<style>
            table.fingering-table { width: 100% !important; border-collapse: collapse; table-layout: fixed; }
            table.fingering-table tr { height: 1.8em !important; }
            table.fingering-table td, table.fingering-table th { padding: 4px 6px !important; font-size: 0.9rem; line-height: 1.5 !important; text-align: center !important; border: 1px solid #ddd; }
            table.fingering-table th { background-color: white; font-weight: bold; }
            table.fingering-table td:first-child { font-weight: bold; background-color: #fafafa; }
            .group-header { background-color: #e8e8e8 !important; font-weight: bold; color: #666; font-size: 0.8rem !important; }
            </style>""", unsafe_allow_html=True)
            
            st.markdown("""<table class="fingering-table">
            <tr><th>调式</th><th>右手指法</th><th>左手指法</th></tr>
            <tr><td class="group-header" colspan="3">基本组（第3指后穿拇指）</td></tr>
            <tr><td>C</td><td>1-2-3-1-2-3-4-5</td><td>5-4-3-5-4-3-2-1</td></tr>
            <tr><td>G</td><td>1-2-3-1-2-3-4-5</td><td>5-4-3-5-4-3-2-1</td></tr>
            <tr><td>D</td><td>1-2-3-1-2-3-4-5</td><td>5-4-3-5-4-3-2-1</td></tr>
            <tr><td>A</td><td>1-2-3-1-2-3-4-5</td><td>5-4-3-5-4-3-2-1</td></tr>
            <tr><td>E</td><td>1-2-3-1-2-3-4-5</td><td>5-4-3-5-4-3-2-1</td></tr>
            <tr><td class="group-header" colspan="3">黑键起步组（拇指不弹黑键）</td></tr>
            <tr><td>Bb</td><td>2-1-2-3-1-2-3-4</td><td>4-5-4-3-5-4-3-2</td></tr>
            <tr><td>Eb</td><td>3-1-2-3-4-1-2-3</td><td>3-5-4-3-2-5-4-3</td></tr>
            <tr><td>Ab</td><td>3-4-1-2-3-1-2-3</td><td>3-2-5-4-3-5-4-3</td></tr>
            <tr><td class="group-header" colspan="3">特殊组（长手指弹黑键，B大调注意穿指）</td></tr>
            <tr><td>B</td><td>1-2-3-1-2-3-4-5</td><td>5-4-3-5-4-3-2-1</td></tr>
            <tr><td>Gb</td><td>2-3-4-1-2-3-1-2</td><td>4-3-2-5-4-3-5-4</td></tr>
            <tr><td>Db</td><td>2-3-1-2-3-4-1-2</td><td>4-3-5-4-3-2-5-4</td></tr>
            <tr><td class="group-header" colspan="3">F大调例外（第4指后穿拇指）</td></tr>
            <tr><td>F</td><td>1-2-3-4-1-2-3-4</td><td>5-4-3-2-5-4-3-2</td></tr>
            </table>""", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
