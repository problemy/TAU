
## About
  Rspec  is the most frequently used testing library for Ruby in production applications based on Ruby on Rails.
  It realizes Behaviour Driven Development and especially Test Driven Development. It also can be used to test 
  less complicated ruby solutions like presented in this tutorial.

  
## Setup
1. Firstly we will need to install Ruby. 
I'm using 2.7.2-devkit in this tutorial, downloaded from https://rubyinstaller.org/downloads/

2. Install Rspec in Command Prompt with Ruby with command :
``` bash
    gem install rspec
```
3.  Init Rspec in Command Prompt with Ruby with command :

``` bash
        rspec --init
```


## Example 
Simple calculator class to test:

``` Ruby
# in lib/calculator.rb
class Calculator
	def add(a, b)
  		a + b
	end
end
```


Simple testing spec
``` Ruby
# in spec/calculator_spec.rb
require "calculator.rb"
RSpec.describe Calculator do
  describe '#add' do
    it 'returns the sum of its arguments' do
      expect(Calculator.new.add(1, 2)).to eq(3)
    end
  end
end
```
Let's focus on the line:

``` Ruby
expect(Calculator.new.add(1, 2)).to eq(3)
```

In this line add method from Calculator class is passed as parameter to method expect(), 
.to is built in Rspec matcher which compare to argument passed to eq() method.

Pseudocode for this test would look like:
```
expect(actual).to be(expected) # test passes if actual.equal?(expected)

```

 "describe" is an RSpec keyword. It depicts the characteristics of the code enclosed in it.

"it" is also a Rspec keyword which is used to define an “Example”.

## Running test
Running tests by their file or directory names is the most familiar way to run tests with RSpec. RSpec can take a file name or directory name and run the file or the contents of the directory.
For example to run our tutorial test:
``` cmd
	 rspec spec/calculator_spec.rb

```

## Output:

  ![Imgur](https://i.imgur.com/4YVAamp.png)

    
