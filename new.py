done = {}
done['name'] = 'ssp'
done['state'] = 'odisha'
done['phone'] = '999000888777'
#print (done)
#print done['name']
#print (done.items())
#print (done.items()[0])
#print (done.items()[0][1])


#print(done.get('name'))
#print(done['name'])

#print(done.get('aadr'))
#print(done['addr'])

#print (done.values())

u_dict = {'name':'Rohan'}
done.update(u_dict)
#print(done)

u_dict = {'name':'Smith'}
#print(done)

u_dict = {'address':'bdk'}
done.update(u_dict)
#print(done)

installer = {}
installer['id'] = "khkjhdj23"
installer['name'] = "Tom"
installer['status'] = 'active'

installer['employees'] = [{'name':'tom','phone'}]
installer['rrason'] = ['underpaid']
installer['complience'] = {"raw":"12-01-1993"}

print installer
print installer['name']







@app.route("/datatypeexp", methods=['GET'])
def datatypeexp():
	#return can't be a list
	
	l = [10,11,12,13,14,15,16,17,18,19]
	ranks = ['priyanka','sid','sundar','david','me']
	ltwo = [20,21,22,23,24,25,26,27,28,29]
	#print (l[0])
	#print (l[0: 6])
	#print (l[0: 6: 2])
	#print (l[:5])
	#print (l[2:])
	#reverse a list
	#print (l-)
	#print (l[::2])
	#print (l[3:1-1])
	#print (l[3::-1])
	#print (l[3:1:-1])
	#slice_object = slice(None,None,1)
	#Start a index 0,stop at end,skip on
	#print (l[slice_object])
	#print (ltwo[slice_object])
	#index = ranks.index('me')
	#print (index)


	#l.append(40)
	#print (l)
    #l.insert(3,367)
    #remove(10)
    #l.pop(2)
    #print len(l)
    #print ranks.count('sundar')
    #brand_new_list = l.copy()
    #print(l)
    #print (brand_new_list)

    #l.clear()
    #print ('l')
    done = {}
    done['name'] = 'ssp'
    done['state'] = 'odisha'
    done['phone'] = '999000888777'

    print done
    #print done['name']

    print done.items()
    print done.items()[0]
    print done.items()[0][1]








	# return needs to be a dict or string
	d = {'somekey':'somevalue'}
	s = 'string'

	return str(l)










