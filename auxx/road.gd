extends Node2D

@export var scroll_speed: float = 400.0
@onready var sprite1 = $RoadSprite1
@onready var sprite2 = $RoadSprite2

# Height of one road sprite in pixels
var sprite_height: float = 630.0  

func _process(delta):
	# Move both sprites downward
	sprite1.position.y += scroll_speed * delta
	sprite2.position.y += scroll_speed * delta

	# If a sprite goes completely off-screen, move it back to the top
	if sprite1.position.y >= sprite_height:
		sprite1.position.y = sprite2.position.y - sprite_height

	if sprite2.position.y >= sprite_height:
		sprite2.position.y = sprite1.position.y - sprite_height
