

def permutations(lst, low, high) :
	out = []
	if (low == high) :
		out.append(lst[low:low+1]);
		return out;

	else :
		for p in permutations(lst, low+1, high):
			print('Now inserting to |> ', p);
			for i in range(len(p)) :
				t = p.copy();
				t.insert(i,lst[low]);
				print('adding |>', t);
				out.append(t);
			t = p.copy();
			t.append(lst[low]);
			out.append(t);
		return out;