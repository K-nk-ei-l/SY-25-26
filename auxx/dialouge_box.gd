extends Control

@export var typing_speed: float = 0.03  # seconds per character

@onready var char_sprite = $Panel/CharacterSprite
@onready var name_label = $Panel/NameLabel
@onready var dialogue_label = $Panel/DialogueLabel

var lines = []         # array of dictionaries for dialogue
var current_line = 0
var is_typing = false
var char_index = 0
var typing_timer = 0.0
var full_text = ""

func start_dialogue(new_lines: Array):
	lines = new_lines
	current_line = 0
	show_line()

func show_line():
	if current_line >= lines.size():
		hide()
		return

	var entry = lines[current_line]
	name_label.text = entry.get("name", "")
	dialogue_label.text = ""
	full_text = entry.get("text", "")
	char_sprite.texture = entry.get("sprite", null)
	char_index = 0
	typing_timer = 0.0
	is_typing = true

func _process(delta):
	if is_typing:
		typing_timer += delta
		if typing_timer >= typing_speed:
			typing_timer = 0.0
			if char_index < full_text.length():
				dialogue_label.text += full_text[char_index]
				char_index += 1
			else:
				is_typing = false

	# Advance dialogue when player presses confirm
	if Input.is_action_just_pressed("ui_accept") and not is_typing:
		current_line += 1
		show_line()
