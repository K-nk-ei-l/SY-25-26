extends CharacterBody2D

@export var lane_offset: float = 130.0   # distance between lanes
@export var slide_speed: float = 8.0    # horizontal slide smoothing
@export var lean_amount: float = 30.0   # max degrees to lean when turning
@export var lean_speed: float = 7.0     # how fast the car returns to straight

var current_lane: int = 0
var target_x: float = 0.0
var target_rotation: float = 0.0

func _process(delta):
	# Handle lane input
	if Input.is_action_just_pressed("ui_left") and current_lane > -1:
		current_lane -= 1
		target_rotation = -lean_amount  # lean left

	elif Input.is_action_just_pressed("ui_right") and current_lane < 1:
		current_lane += 1
		target_rotation = lean_amount   # lean right

	# Calculate target x based on lane
	target_x = current_lane * lane_offset

	# Smoothly slide horizontally
	position.x = lerp(position.x, target_x, delta * slide_speed)

	# Smoothly rotate back to straight (0)
	target_rotation = lerp(target_rotation, 0.0, delta * lean_speed)
	rotation_degrees = target_rotation
