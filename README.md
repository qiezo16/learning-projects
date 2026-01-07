# Tower-of-Hanoi
My attempt at making a tower of Hanoi game ( made after learning how to complete LinkedList, DoublyLinkedList, Nodes and Stacks

I made this after learning the above in a week with some direction. I got stuck multiple times espcially in the get_input function where the options would infinetely repeat and never actually save moves,
Still got to work on some syntax practice because i mainly think too fast and forget to run functions as an action and getting the return value rather than just calling back functions without the parenthesis.

Jesus christ finally, i spent all afternoon trying to figure out why it wouldnt save my moves, i knew there was something wrong with my get_input function. I combined lines 35, 36, 37 into one because fuck all that.
I also removed the choices[i] in my intial get input line 39 beacause it was checking substring membership and not lsit membership. Added a statement in case an incorrect input was inputted. Lastly in in 58 - 61 my disk comparison logic was wrong.