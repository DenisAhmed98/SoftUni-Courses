from unittest import TestCase, main
from project.social_media import SocialMedia

class TestSocialMedia(TestCase):
    def setUp(self) -> None:
        self.user1 = ("TestUser","YouTube",100,"Vlog")

    def test_social_media_correct_init(self):
        user1 = SocialMedia("Test","YouTube",100,"Vlog")
        self.assertEqual(user1._username, "Test")
        self.assertEqual(user1._platform, "YouTube")
        self.assertEqual(user1._followers, 100)
        self.assertEqual(user1._content_type, "Vlog")
        self.assertEqual(user1._posts, [])

    def test_platform_validation_expected_error(self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        with self.assertRaises(ValueError) as ve:
            user = SocialMedia("Test","Wrong",100,"Vlog")
        self.assertEqual(str(ve.exception), f"Platform should be one of {allowed_platforms}")
    
    def test_followers_validation_expected_error(self):
        user = SocialMedia("Test","YouTube",100,"Vlog")
        with self.assertRaises(ValueError) as ve:
            user.followers = -5
             
            

        self.assertEqual(str(ve.exception), "Followers cannot be negative.") 

    def test_create_post(self):
        user = SocialMedia("Test","YouTube",100,"Vlog")
        ex = user.create_post("Post_Content")
        post = [{'content': 'Post_Content', 'likes': 0, 'comments': []}]

        self.assertEqual(ex, f"New {user._content_type} post created by {user._username} on {user._platform}.")
        self.assertEqual(user._posts,post)
    
    def test_like_post_with_correct_data_with_less_than_10_likes(self):
        user = SocialMedia("Test","YouTube",100,"Vlog")
        user.create_post("Post_Content")
        ex = user.like_post(0)
        post = user._posts[0]

        self.assertEqual(ex, f"Post liked by {user._username}.")
        self.assertEqual(post['likes'],1)
    
    def test_like_post_with_correct_data_with_more_than_10_likes(self):
        user = SocialMedia("Test","YouTube",100,"Vlog")
        user.create_post("Post_Content")
        user._posts[0]["likes"] = 10

        ex = user.like_post(0)
        
        self.assertEqual(ex, f"Post has reached the maximum number of likes.")
        self.assertEqual(user._posts[0]["likes"],10)
    
    def test_like_post_with_wrong_index(self):
        user = SocialMedia("Test","YouTube",100,"Vlog")
        user.create_post("Post_Content")
        post = [{'content': 'Post_Content', 'likes': 0, 'comments': []}]

        ex = user.like_post(5)
        
        self.assertEqual(ex, "Invalid post index.")
        self.assertEqual(user._posts,post)
    
    def test_comment_on_post_correct_data(self):
        user = SocialMedia("Test","YouTube",100,"Vlog")
        user.create_post("Post_Content")
        ex = user.comment_on_post(0,"Test Test!!!")
        comment = user._posts[0]['comments']
        comment_check = [{'user': 'Test', 'comment': 'Test Test!!!'}]
        self.assertEqual(ex, f"Comment added by {user._username} on the post.")
        self.assertEqual(comment, comment_check)
    
    def test_comment_on_post_with_less_than_10_characters(self):
        user = SocialMedia("Test","YouTube",100,"Vlog")
        user.create_post("Post_Content")
        ex = user.comment_on_post(0,"0000")
        comment = user._posts[0]['comments']
        self.assertEqual(ex, "Comment should be more than 10 characters.")
        self.assertEqual(comment, [])








        


        



if __name__ == "__main__":
    main()