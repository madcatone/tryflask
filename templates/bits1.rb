#bits1.rb
#Ruby bits(2) method and class
def get_tweets(list)
	if list.authorized?(@user)
		list.get_tweets
	else
		[]
	end
end
#class getter and setter
class Name
	def initialize(first, last = nil)
		@first = first
		@last = last
	end
	def format
		[@last, @first].compact.join(', ')
	end
end

#oversharing
class Tweet
	attr_accessor :status
	attr_reader :created_at
	def initialize(status)
		@status = status
		@created_at = Time.new
	end
	#re-open class
	def to_s
		"#{@status}\n#{created_at}"
	end
end

class UserList
	attr_accessor :name
	def initialize(name)
		#self means set current object
		self.name = name
	end
end

list = UserList.new('claire')
puts list.name

#user_name = []
#user_name << Name.new('Ash', 'Ken')
#user_name << Name.new('Eth', 'Mad')
#user_name << Name.new('Far')
#user_name.each { |n| puts n.format }


tweet = Tweet.new("Take a shower.")
#tweet.created_at = Time.new(2084, 1, 1, 0, 0, 0, "-07:00")
puts tweet.to_s
