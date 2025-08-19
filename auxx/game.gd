extends Node2D
func _ready():
	# Example dialogue
	var dialogue = [
		{
			"name": "Alice",
			"text": "We finally made it to the city!",
			"sprite": preload("res://download (1).jpg")
		},
		{
			"name": "Bob",
			"text": "Yes... but something feels off here.",
			"sprite": preload("res://download.jpg")
		}
	]
	
	# Run the dialogue
	$DialogueBox.start_dialogue(dialogue)
	$DialogueBox.visible = true
