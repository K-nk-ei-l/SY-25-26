extends Node2D
func _ready():
	# Example dialogue
	var dialogue = [
		{
			"name": "Alice",
			"text": "This is a test text box!",
			"sprite": preload("res://download (1).jpg")
		},
		{
			"name": "Bob",
			"text": "A test box if you will! Heh.",
			"sprite": preload("res://download.jpg")
		}
	]
	
	# Run the dialogue
	$DialogueBox.start_dialogue(dialogue)
	$DialogueBox.visible = true
