
fitness_influencer = str(input("fitness influencer name: "))
first_name = fitness_influencer.split(" ")[0]
last_name = fitness_influencer.split(" ")[-1]

gym_goal = str(input("gym goal: ")) # E.g, Muscle-building , toning, Strength

muscle_1 = str(input("1 muscle: "))
muscle_2 = str(input("2 muscle: "))
muscle_3 = str(input("3 muscle: "))
muscle_4 = str(input("4 muscle: "))




muscle_group = [muscle_1, muscle_2, muscle_3, muscle_4]# Arms, Back, Leg (Only 3)
number_of_splits_per_week = str(input("splits per week? "))
gender = str(input("His or Her? "))

print(f"{fitness_influencer}'s Workout Routine – Achieve {first_name}'s Physique!")


article_html = '''
<!-- wp:paragraph -->
<p>Welcome to ''' + fitness_influencer + '''\'s ''' + gym_goal + ''' Workout Routine, where we detail ''' + gender + ''' workout and methods! Check out our highlighted workouts:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><!-- wp:list-item -->
<li>''' + fitness_influencer + '''\'s ''' + gym_goal + ''' ''' + muscle_group[0] + ''' Workout</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>''' + fitness_influencer + '''\'s ''' + gym_goal + ''' ''' + muscle_group[1] + ''' Workout</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>''' + fitness_influencer + '''\'s ''' + gym_goal + ''' ''' + muscle_group[2] + ''' Workout</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:list-item -->
<li>''' + fitness_influencer + '''\'s ''' + gym_goal + ''' ''' + muscle_group[3] + ''' Workout</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2 class="wp-block-heading"><strong>About ''' + fitness_influencer + '''\'s Program</strong></h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>''' + first_name + f''' follows a {number_of_splits_per_week}-day split routine, focusing on ''' + ", ".join(muscle_group) + '''</p>
<!-- /wp:paragraph -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:paragraph {"backgroundColor":"cyan-bluish-gray"} -->
<p class="has-cyan-bluish-gray-background-color has-background">Looking to follow ''' + fitness_influencer + '''\'s workout routine? Click <a href="https://pumpx.app/">Here</a> To Download PumpX and easily add ''' + fitness_influencer + '''\'s exercises to your workout!</p>
<!-- /wp:paragraph -->
'''

with open("ads.txt", 'w', newline="") as f:
    f.write(article_html)



#research claire northfield and find information about her workout routine and fill it in html table accoordingly, if you dont know sets or reps just add in some arbitrary number, add more or less rows depending on number of exercises

workout_table =f"""
<!-- wp:heading -->
<h2 class="wp-block-heading">{first_name}'s {muscle_group[0]} Workout</h2>
<!-- /wp:heading -->

<!-- wp:table -->
<figure class="wp-block-table"><table><tbody><tr><td><strong>Exercises</strong></td><td><strong>Sets</strong></td><td><strong>Reps</strong></td></tr><tr><td><strong>Incline Smith Machine Press</strong></td><td>4-6 sets till failure</td><td>6-8 rep range</td></tr><tr><td><strong>Cable Chest Fly’s</strong></td><td>4-5 sets till failure</td><td>10-15 rep range</td></tr><tr><td><strong>Pec Deck</strong></td><td>1 set till failure</td><td>8-12 rep range</td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:heading -->
<h2 class="wp-block-heading">{first_name}'s {muscle_group[1]} Workout</h2>
<!-- /wp:heading -->

<!-- wp:table -->
<figure class="wp-block-table"><table><tbody><tr><td><strong>Exercises</strong></td><td><strong>Sets</strong></td><td><strong>Reps</strong></td></tr><tr><td><strong>Straight-Bar Triceps Pushdown/Extension</strong></td><td>4 sets till failure</td><td>Till Failure</td></tr><tr><td><strong>Overhead Cable Triceps Extension</strong></td><td>3 sets to failure</td><td>Till Failure</td></tr><tr><td><strong>Cross Cable Triceps Extension</strong></td><td>1 set to failure</td><td>Till Failure</td></tr><tr><td><strong>Standing Hammer Curls</strong></td><td>2 heavy sets to failure</td><td>Till Failure</td></tr><tr><td><strong>Machine Bicep Curl</strong></td><td>3 sets to failure</td><td>Till Failure</td></tr><tr><td><strong>EZ Bar Curls</strong></td><td>2 sets to failure</td><td>Till Failure</td></tr><tr><td><strong>Dumbbell Preacher Curls</strong></td><td>2 sets to failure</td><td>Till Failure</td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:separator -->
<hr class="wp-block-separator has-alpha-channel-opacity"/>
<!-- /wp:separator -->

<!-- wp:heading -->
<h2 class="wp-block-heading">{first_name}'s {muscle_group[2]} Workout</h2>
<!-- /wp:heading -->

<!-- wp:table -->
<figure class="wp-block-table"><table><tbody><tr><td><strong>Exercises</strong></td><td><strong>Sets</strong></td><td><strong>Reps</strong></td></tr><tr><td>Seated Leg Hamstring Curl</td><td>4 Sets (1 warm up, 3 working sets)</td><td>15-30 reps for warm up.  8-15 reps for working sets</td></tr><tr><td>Cable Romanian Deadlifts</td><td>3 Sets till failure</td><td>8-12 rep range</td></tr><tr><td>Narrow-Stance Barbell Squat</td><td>4 Sets till failure</td><td>8-12 rep range</td></tr><tr><td>Quad Extensions (Leg Extensions)</td><td>4 Sets till failure</td><td>8-15 rep range</td></tr></tbody></table></figure>
<!-- /wp:table -->


<!-- wp:heading -->
<h2 class="wp-block-heading">{first_name}'s {muscle_group[3]} Workout</h2>
<!-- /wp:heading -->

<!-- wp:table -->
<figure class="wp-block-table"><table><tbody><tr><td><strong>Exercises</strong></td><td><strong>Sets</strong></td><td><strong>Reps</strong></td></tr><tr><td>Seated Leg Hamstring Curl</td><td>4 Sets (1 warm up, 3 working sets)</td><td>15-30 reps for warm up.  8-15 reps for working sets</td></tr><tr><td>Cable Romanian Deadlifts</td><td>3 Sets till failure</td><td>8-12 rep range</td></tr><tr><td>Narrow-Stance Barbell Squat</td><td>4 Sets till failure</td><td>8-12 rep range</td></tr><tr><td>Quad Extensions (Leg Extensions)</td><td>4 Sets till failure</td><td>8-15 rep range</td></tr></tbody></table></figure>
<!-- /wp:table -->


"""

#promtp
# fill in the template for what to expect from this workout specific to {fitness_influencer} make it hyper specific to characteristics and personality

what_to_expect =''' #prompt
<!-- wp:heading -->
<h2 class="wp-block-heading">What To Expect From This Program</h2>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Brodie Falgoust's program is a dynamic and intense fitness journey, focusing on building muscle and shredding fat. You'll start with high-intensity workouts like Incline Smith Machine Press and Cable Chest Fly’s, designed to build chest muscles, along with arm workouts for bicep and tricep development.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph -->
<p>The program, suitable for all fitness levels, incorporates a push, pull, legs split, ensuring comprehensive body development. The progressive structure will challenge you to gradually increase intensity, maximizing muscle growth and endurance.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph -->
<p>Embrace a routine that combines rigorous training with strategic rest, reflecting Brodie's own fitness philosophy. Get ready for a transformation, not just in physique but also in strength and overall fitness, mirroring the success of renowned fitness personalities.</p>
<!-- /wp:paragraph -->

'''

# prompt 
# create this faq block specific to claire and questions that people would actually search for SEO(Keep Questions short aswell) make it hyper specific to characteristics and personality:

faq_block = """
<!-- wp:wpseopress/faq-block {"faqs":[{"question":"<strong><strong>How does Sam Sulek build muscle mass?</strong></strong>","answer":"Focus on hypertrophy - Sam's routine is all about muscle growth and sculpting.","image":""},{"question":"<strong>What exercises are in Sam Sulek’s chest routine?</strong>","answer":"Includes Incline Smith Machine Press, Cable Chest Fly, and Pec Deck for comprehensive chest development.","image":""},{"question":"<strong>What is Sam Sulek’s diet for muscle building?</strong>","answer":"A diverse, high-calorie diet, balancing intense workouts with occasional indulgences.","image":""},{"question":"<strong>Does Sam Sulek include cardio in his workout plan?</strong>","answer":"Yes, a consistent 30-minute daily cardio session, often cycling, for overall fitness.","image":""},{"question":"<strong>Why is Sam Sulek’s workout method unique?</strong>","answer":"His flexible exercise selection and unique diet choices set his routine apart.","image":""},{"question":"<strong>What supplements does Sam Sulek recommend for fitness?</strong>","answer":"Protein shakes are a key component for muscle growth and recovery in his regimen.","image":""},{"question":"<strong>What results has Sam Sulek achieved with his workout commitment?</strong>","answer":"A testament to dedication - Sam’s physique is both impressive and distinctive.","image":""},{"question":"<strong>What makes Sam Sulek a standout fitness influencer?</strong>","answer":"His unconventional approach and unique video style offer a fresh perspective in fitness.","image":""},{"question":"<strong>What can we learn from Sam Sulek’s fitness journey?</strong>","answer":"His journey exemplifies the impact of perseverance and dedication on physical transformation.","image":""},{"question":"<strong>How effective is Sam Sulek’s workout and diet for personal fitness goals?</strong>","answer":"Incorporating his high-volume training and varied diet can significantly benefit your own fitness journey.","image":""}]} /-->
"""
