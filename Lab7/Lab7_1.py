import ArrayStack


def get_tag(inExp) :
	inExp = inExp.strip();
	terminateN = len(inExp);
	curN = 0;

	while curN < terminateN :

		if inExp[curN] == '<' :
			tagArr = [];

			while inExp[curN] != '>' :

				if(inExp[curN] == ' ') :
					while inExp[curN] != '>' :
						curN += 1
					if inExp[curN-1] == '/' :
						curN -= 1

				else :
					tagArr.append(inExp[curN]);
					curN += 1;

			tagArr.append(inExp[curN]);
			yield ''.join(tagArr);
		else :
			curN += 1



def is_matched_tags(inExp) :
	tagsS = ArrayStack.Stack()
	tagsE = ArrayStack.Stack()

	for tag in get_tag(inExp) :
		tagsS.push(tag);

	while not tagsS.is_empty():
		single = False;
		if(tagsS.top()[-2] == '/') :
			print('SINGULAR TAG :', tagsS.top())
			tagsS.pop();
			single = True;
		if(tagsS.top()[1] == '!') :
			print('! TAG:', tagsS.top())
			tagsS.pop();
			single = True


		if not tagsS.is_empty() and not single:

			if(tagsE.is_empty()) :
				tagsE.push(tagsS.pop());

			target = tagsE.top()[0] + tagsE.top()[2:];

			if(tagsS.top() == target) :
				print('MATCHED TAGS :', target);
				tagsE.pop();
				tagsS.pop();
			else :
				tagsE.push(tagsS.pop());

	if(tagsE.is_empty()) :
		return True
	else :
		print()
		print()
		print(tagsE);
		print()
		print(tagsS);
		return False













testHTML = '''
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Style-Type" content="text/css" /> 
    <title>html_file.html</title>
    <link href="/library/skin/tool_base.css" type="text/css" rel="stylesheet" media="all" />
    <link href="/library/skin/morpheus-nyu/tool.css" type="text/css" rel="stylesheet" media="all" />
    <script type="text/javascript" src="/library/js/headscripts.js"></script>
<script type="text/javascript" src="/media-gallery-tool/js/kaltura-upgrade.js"></script>    <style>body { padding: 5px !important; }</style>
  </head>
  <body>
<body> 
<center> 
<h1> The Little Boat </h1> 
</center> 
<p> The storm tossed the little 
boat like a cheap sneaker in an 
old washing machine. The three 
drunken fishermen were used to 
such treatment, of course, but 
not the tree salesman, who even as 
a stowaway now felt that he 
had overpaid for the voyage. </p> 
<ol> 
<li> Will the salesman die? </li> 
<li> What color is the boat? </li> 
<li> And what about Naomi? </li> 
</ol> 
</body> 
  </body>
</html>
'''

print(is_matched_tags(testHTML));