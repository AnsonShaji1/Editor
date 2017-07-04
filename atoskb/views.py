from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post
from django.core.files.storage import FileSystemStorage
import os
import os.path
from mysite.settings import BASE_DIR
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
#from bs4 import BeautifulSoup
import re
import unicodedata
#from PIL import Image
# import magic
#from thumbnails import get_thumbnail
#sys.setdefaultencoding('utf-8')
def post_table(request):
    #import pdb;pdb.set_trace()
    folder_names=os.listdir(BASE_DIR +'/All_contents')
    dic_filenames = {}
    for f_name in folder_names:
        new_path = BASE_DIR +"/All_contents/" + f_name
        array_sub_topic1=os.listdir(new_path)
        array_sub_topic2=[]

        for item in array_sub_topic1:
            item=item.replace('.xml','')
            array_sub_topic2.append(item)
        dic_filenames[f_name] = array_sub_topic2
    if request.method == 'GET':

        return render(request,'atoskb/first.html',{'dic_filenames':dic_filenames})



def post_list(request):

    if request.method == 'POST':
        #print request.POST
        #import pdb;pdb.set_trace()
        h_id = request.POST.get('h_id1')
        if h_id =='':
            #my_image=request.FILES['datafile']
            #h_id = request.POST.get('h_id1')
            topic=request.POST.get('topic')
            tvar=request.POST.get('tvariations') # u'hai,how are you,fine uu,uu uu' 
            tvar=unicodedata.normalize('NFKD', tvar).encode('ascii','ignore')  #'hai,how are you,fine uu,uu uu'

            subtopic=request.POST.get('subtopic')
            #F_subtopic=re.sub(' ','_',subtopic)
            svar=request.POST.get('svariations')  # u'how old are you,humen,humen huju'
            svar=unicodedata.normalize('NFKD', svar).encode('ascii','ignore')  # 'how old are you,humen,humen huju'

            short=request.POST.get('short')
            #possiblequestion=request.POST.get('possiblequestion')
            possiblequestion=request.POST.get('possible')
            possiblequestion=unicodedata.normalize('NFKD', possiblequestion).encode('ascii','ignore')


            
            #import pdb;pdb.set_trace()
            ckeditor=request.POST.get('ckeditor')



            for count, x in enumerate(request.FILES.getlist("datafile")):
                def process(f):                    
                    with open(BASE_DIR+'/atoskb/static/uploads/'+str(topic)+str(subtopic)+str(x.name),'wb+') as destination:
                        #print x.content_type
                        for chunk in f.chunks():
                            destination.write(chunk)                            
                process(x)

            #import pdb;pdb.set_trace()
            dic_file_types={'JPEG':'.jpg','GIF':'.gif','ISO Media, MPEG':'.mp4','ASCII text':'.txt','MPEG ADTS':'.mp3','OpenDocument Spreadsheet':'.ods'}
            #dic_file_types={'ASCII text':'.txt'}
            image_folder=os.listdir(BASE_DIR +'/atoskb/static/uploads/')
            list_image_folder=[]
            # for item in image_folder:
            #     if str(topic)+str(subtopic) in item:
            #         filename, file_extension = os.path.splitext(BASE_DIR +'/atoskb/static/uploads/'+item)
            #         flag=0
            #         if file_extension == '':
            #             file_type=magic.from_file(filename)
            #             for i in dic_file_types.keys():
            #                 if i in file_type:
            #                     flag=1
            #                     extension=dic_file_types[i]
            #                     item3=item+extension
            #                     list_image_folder.append(item3)
            #                     image3=BASE_DIR+'/atoskb/static/uploads/'+str(item)                  
            #                     image4=BASE_DIR+'/atoskb/static/uploads/'+str(item3)
            #                     os.system('mv "'+image3+'" "'+image4+'"')
            #                 else:
            #                     pass
            #             if not flag:
            #                 list_image_folder.append(item)
            #         else:
            #             list_image_folder.append(item)
            #     else:
            #         pass            

            





            dirName=BASE_DIR+'/All_contents/'+str(topic)
            #print dirName
            if not os.path.exists(dirName):
                os.mkdir(dirName)
            else:
                pass


            xmlName=BASE_DIR+'/All_contents/'+str(topic)+'/'+str(subtopic)+'.xml'

            file2=open(xmlName,"w")

            toFile1='<?xml version="1.0" encoding="UTF-8"?><Data><topic>Topic:'+str(topic)+'</topic><Variations1>'+str(tvar)+'</Variations1><Sub_topic>'+str(subtopic)+'</Sub_topic><Variations2>'+str(svar)+'</Variations2><Short_description>'+str(short)+'</Short_description><Possible_question>'+str(possiblequestion)+'</Possible_question><ckeditor>'+str(ckeditor)+'</ckeditor><image>'+str(list_image_folder)+'</image></Data>'
            file2.write(toFile1)
            file2.close()
            #import pdb;pdb.set_trace()

            args=Post.objects.create(topic=topic, var1=tvar, sub_topic=str(subtopic),var2=svar,short=short,possible=possiblequestion,ck=ckeditor,image=list_image_folder)

            #import pdb;pdb.set_trace()

            # folder_names=os.listdir(BASE_DIR +'/All_contents')
            # dic_filenames = {}
            # for f_name in folder_names:
            #     new_path = BASE_DIR +"/All_contents/" + f_name
            #     array_sub_topic1=os.listdir(new_path)
            #     array_sub_topic2=[]

            #     for item in array_sub_topic1:
            #         item=item.replace('.xml','')
            #         array_sub_topic2.append(item)
            #     dic_filenames[f_name] = array_sub_topic2

            #return redirect(request,'atoskb/first.html',{'dic_filenames':dic_filenames})
            return redirect('/')

        if h_id !='':
            #import pdb;pdb.set_trace()
            image_list=[]
            image_list1=request.POST.get('h_id2')
            image_list1=unicodedata.normalize('NFKD', image_list1).encode('ascii','ignore')
            ##image_list=image_list.replace("['",'').replace("', '",',').replace("']",'').split(',')
            image_list1=image_list1.split(',')
            for i in image_list1:
                if isinstance(i, unicode):
                    i=unicodedata.normalize('NFKD', i).encode('ascii','ignore')
                    image_list.append(i)
                else:
                    image_list.append(i)


            #image=re.sub(r" ","",image)
            #aj_topic=request.POST.get('test_topic')
            aj_tvar=request.POST.get('tvar_1')   
            aj_tvar=unicodedata.normalize('NFKD', aj_tvar).encode('ascii','ignore')  
            aj_subtopic=request.POST.get('sub_var_1')

            #F_aj_subtopic=re.sub(' ','_',aj_subtopic)

            aj_svar=request.POST.get('sub_var_2') 
            aj_svar=unicodedata.normalize('NFKD', aj_svar).encode('ascii','ignore') 

            aj_short=request.POST.get('short_1')
            aj_possible=request.POST.get('possi_1')
            aj_possible=unicodedata.normalize('NFKD', aj_possible).encode('ascii','ignore')
            aj_ckeditor=request.POST.get('ckeditor_1')



            topic=request.POST.get('test_topic')       
            tvar=request.POST.get('tvariations')  
            tvar=unicodedata.normalize('NFKD',tvar).encode('ascii','ignore')  
            subtopic=request.POST.get('subtopic')
            #F_subtopic=re.sub(' ','_',subtopic)

            svar=request.POST.get('svariations') 
            svar=unicodedata.normalize('NFKD',svar).encode('ascii','ignore') 

            short=request.POST.get('short')
            possiblequestion=request.POST.get('possible')
            possiblequestion=unicodedata.normalize('NFKD',possiblequestion).encode('ascii','ignore')

            ckeditor=request.POST.get('ckeditor')
            len_ckeditor=len(ckeditor)
            ckeditor=ckeditor[:len_ckeditor-2]

            
            if('datafile' in request.FILES) and aj_subtopic != subtopic:


                New_item1=Post.objects.get(id=h_id)
                New_item1.delete()
                xmlName=BASE_DIR+'/All_contents/'+str(topic)+'/'+str(aj_subtopic)+'.xml'
                os.system('rm "'+xmlName+'"')


                for count, x in enumerate(request.FILES.getlist("datafile")):
                    def process(f):
                        #import pdb;pdb.set_trace()
                        with open(BASE_DIR+'/atoskb/static/uploads/'+str(topic)+str(subtopic)+str(x.name),'wb+') as destination:
                            
                            for chunk in f.chunks():
                                destination.write(chunk)                                
                    process(x)






                rename_list=[]
                for item in image_list:
                    item=item.replace(topic+aj_subtopic,topic+subtopic).replace("u'","'")
                    rename_list.append(item)

                for i,j in zip(image_list,rename_list):
                    image1=BASE_DIR+'/atoskb/static/uploads/'+str(i)                   
                    image2=BASE_DIR+'/atoskb/static/uploads/'+str(j)
                    os.system('mv "'+image1+'" "'+image2+'"')
                   



                dic_file_types={'JPEG':'.jpg','GIF':'.gif','ISO Media, MPEG':'.mp4','ASCII text':'.txt','MPEG ADTS':'.mp3','OpenDocument Spreadsheet':'.ods'}
                image_folder=os.listdir(BASE_DIR +'/atoskb/static/uploads/')
                list_image_folder=[]
                # for item in image_folder:
                #     if str(topic)+str(subtopic) in item:
                #         filename, file_extension = os.path.splitext(BASE_DIR +'/atoskb/static/uploads/'+item)
                #         flag=0
                #         if file_extension == '':
                #             file_type=magic.from_file(filename)
                #             for i in dic_file_types.keys():
                #                 if i in file_type:
                #                     flag=1
                #                     extension=dic_file_types[i]
                #                     item3=item+extension
                #                     list_image_folder.append(item3)
                #                     image3=BASE_DIR+'/atoskb/static/uploads/'+str(item)                  
                #                     image4=BASE_DIR+'/atoskb/static/uploads/'+str(item3)
                #                     os.system('mv "'+image3+'" "'+image4+'"')
                #                 else:
                #                     pass
                #             if not flag:
                #                 list_image_folder.append(item)
                #         else:
                #             list_image_folder.append(item)
                #     else:
                #         pass




                dirName=BASE_DIR+'/All_contents/'+str(topic)
                xmlName=BASE_DIR+'/All_contents/'+str(topic)+'/'+str(subtopic)+'.xml'
                
                #import pdb;pdb.set_trace()
                file2=open(str(xmlName),"w")
                toFile1='<?xml version="1.0" encoding="UTF-8"?><Data><topic>Topic:'+str(topic)+'</topic><Variations1>'+str(tvar)+'</Variations1><Sub_topic>'+str(subtopic)+'</Sub_topic><Variations2>'+str(svar)+'</Variations2><Short_description>'+str(short)+'</Short_description><Possible_question>'+str(possiblequestion)+'</Possible_question><ckeditor>'+str(ckeditor)+'</ckeditor><image>'+str(list_image_folder)+'</image></Data>'
                
                file2.write(toFile1)
                file2.close()
                args=Post.objects.create(topic=topic,var1=tvar,sub_topic=str(subtopic),var2=svar,short=short,possible=possiblequestion,ck=ckeditor,image=list_image_folder)


                return redirect('/')



            elif('datafile' in request.FILES) and aj_subtopic == subtopic:

 
                New_item1=Post.objects.get(id=h_id)
                New_item1.delete()
                xmlName=BASE_DIR+'/All_contents/'+str(topic)+'/'+str(aj_subtopic)+'.xml'
                os.system('rm "'+xmlName+'"')
                
                for count, x in enumerate(request.FILES.getlist("datafile")):
                    def process(f):
                        with open(BASE_DIR+'/atoskb/static/uploads/'+str(topic)+str(subtopic)+str(x.name),'wb+') as destination:                            
                            for chunk in f.chunks():
                                destination.write(chunk)
                            
                    process(x)





                #dic_file_types={'JPEG':'.jpg','GIF':'.gif','PNG':'.png'}
                dic_file_types={'JPEG':'.jpg','GIF':'.gif','ISO Media, MPEG':'.mp4','ASCII text':'.txt','MPEG ADTS':'.mp3','OpenDocument Spreadsheet':'.ods'}
                #dic_file_types={'JPEG':'.jpg','GIF':'.gif','PNG':'.png','ISO Media, MPEG':'.mp4','python 2.7 byte-compiled':'.pyc','Python script':'.py','ASCII text':'.txt','MPEG ADTS':'.mp3','OpenDocument Spreadsheet':'.ods'}
                image_folder=os.listdir(BASE_DIR +'/atoskb/static/uploads/')
                list_image_folder=[]
                # for item in image_folder:
                #     if str(topic)+str(subtopic) in item:
                #         filename, file_extension = os.path.splitext(BASE_DIR +'/atoskb/static/uploads/'+item)
                #         flag=0
                #         if file_extension == '':
                #             file_type=magic.from_file(filename)
                #             for i in dic_file_types.keys():
                #                 if i in file_type:
                #                     flag=1
                #                     extension=dic_file_types[i]
                #                     item3=item+extension
                #                     list_image_folder.append(item3)
                #                     image3=BASE_DIR+'/atoskb/static/uploads/'+str(item)                  
                #                     image4=BASE_DIR+'/atoskb/static/uploads/'+str(item3)
                #                     os.system('mv "'+image3+'" "'+image4+'"')
                #                 else:
                #                     pass
                #             if not flag:
                #                 list_image_folder.append(item)
                #         else:
                #             list_image_folder.append(item)
                #     else:
                #         pass




                dirName=BASE_DIR+'/All_contents/'+str(topic)
                xmlName=BASE_DIR+'/All_contents/'+str(topic)+'/'+str(subtopic)+'.xml'
                
                file2=open(str(xmlName),"w")
                toFile1='<?xml version="1.0" encoding="UTF-8"?><Data><topic>Topic:'+str(topic)+'</topic><Variations1>'+str(tvar)+'</Variations1><Sub_topic>'+str(subtopic)+'</Sub_topic><Variations2>'+str(svar)+'</Variations2><Short_description>'+str(short)+'</Short_description><Possible_question>'+str(possiblequestion)+'</Possible_question><ckeditor>'+str(ckeditor)+'</ckeditor><image>'+str(list_image_folder)+'</image></Data>'
                
                file2.write(toFile1)
                file2.close()
                args=Post.objects.create(topic=topic,var1=tvar,sub_topic=str(subtopic),var2=svar,short=short,possible=possiblequestion,ck=ckeditor,image=list_image_folder)



                return redirect('/')


            elif('datafile' not in request.FILES) and aj_subtopic != subtopic:

                New_item1=Post.objects.get(id=h_id)
                New_item1.delete()
                xmlName=BASE_DIR+'/All_contents/'+str(topic)+'/'+str(aj_subtopic)+'.xml'
                os.system('rm "'+xmlName+'"')                

                #import pdb;pdb.set_trace()
                rename_list=[]
                for item in image_list:
                    item=item.replace(topic+aj_subtopic,topic+subtopic).replace("u'","'")
                    rename_list.append(item)

                for i,j in zip(image_list,rename_list):
                    image1=BASE_DIR+'/atoskb/static/uploads/'+str(i)                   
                    image2=BASE_DIR+'/atoskb/static/uploads/'+str(j)
                    os.system('mv "'+image1+'" "'+image2+'"')
                   



                image_folder=os.listdir(BASE_DIR +'/atoskb/static/uploads/')
                list_image_folder=[]
                for item in image_folder:
                    if str(topic)+str(subtopic) in item:
                        list_image_folder.append(item)
                    else:
                        pass





                dirName=BASE_DIR+'/All_contents/'+str(topic)
                xmlName=BASE_DIR+'/All_contents/'+str(topic)+'/'+str(subtopic)+'.xml'
                
                #import pdb;pdb.set_trace()
                file2=open(str(xmlName),"w")
                toFile1='<?xml version="1.0" encoding="UTF-8"?><Data><topic>Topic:'+str(topic)+'</topic><Variations1>'+str(tvar)+'</Variations1><Sub_topic>'+str(subtopic)+'</Sub_topic><Variations2>'+str(svar)+'</Variations2><Short_description>'+str(short)+'</Short_description><Possible_question>'+str(possiblequestion)+'</Possible_question><ckeditor>'+str(ckeditor)+'</ckeditor><image>'+str(list_image_folder)+'</image></Data>'
                
                file2.write(toFile1)
                file2.close()
                args=Post.objects.create(topic=topic,var1=tvar,sub_topic=str(subtopic),var2=svar,short=short,possible=possiblequestion,ck=ckeditor,image=list_image_folder)

                # folder_names=os.listdir(BASE_DIR +'/All_contents')
                # dic_filenames = {}
                # for f_name in folder_names:
                #     new_path = BASE_DIR +"/All_contents/" + f_name
                #     array_sub_topic1=os.listdir(new_path)
                #     array_sub_topic2=[]

                #     for item in array_sub_topic1:
                #         item=item.replace('.xml','')
                #         array_sub_topic2.append(item)
                #     dic_filenames[f_name] = array_sub_topic2

                #return render(request,'atoskb/first.html',{'dic_filenames':dic_filenames})
                return redirect('/')
            
            else:
                #import pdb;pdb.set_trace()
                if svar != aj_svar or tvar != aj_tvar or aj_short != short or aj_possible != possiblequestion or aj_ckeditor != ckeditor:
                    #New_item1=Post.objects.get(sub_topic=aj_subtopic,topic=aj_topic)
                    New_item1=Post.objects.get(id=h_id)
                    New_item1.delete()
                    xmlName=BASE_DIR+'/All_contents/'+str(topic)+'/'+str(aj_subtopic)+'.xml'
                    os.system('rm "'+xmlName+'"')


                    dirName=BASE_DIR+'/All_contents/'+str(topic)
                    xmlName=BASE_DIR+'/All_contents/'+str(topic)+'/'+str(subtopic)+'.xml'

                    file2=open(str(xmlName),"w")
                    toFile1='<?xml version="1.0" encoding="UTF-8"?><Data><topic>Topic:'+str(topic)+'</topic><Variations1>'+str(tvar)+'</Variations1><Sub_topic>'+str(subtopic)+'</Sub_topic><Variations2>'+str(svar)+'</Variations2><Short_description>'+str(short)+'</Short_description><Possible_question>'+str(possiblequestion)+'</Possible_question><ckeditor>'+str(ckeditor)+'</ckeditor><image>'+str(image_list)+'</image></Data>'
            
                    #import pdb;pdb.set_trace()
                    file2.write(toFile1)
                    file2.close()
                    args=Post.objects.create(topic=topic,var1=tvar,sub_topic=str(subtopic),var2=svar,short=short,possible=possiblequestion,ck=ckeditor,image=image_list)


                    # folder_names=os.listdir(BASE_DIR +'/All_contents')
                    # dic_filenames = {}
                    # for f_name in folder_names:
                    #     new_path = BASE_DIR +"/All_contents/" + f_name
                    #     array_sub_topic1=os.listdir(new_path)
                    #     array_sub_topic2=[]

                    #     for item in array_sub_topic1:
                    #         item=item.replace('.xml','')
                    #         array_sub_topic2.append(item)
                    #     dic_filenames[f_name] = array_sub_topic2

                    #return render(request,'atoskb/first.html',{'dic_filenames':dic_filenames})
                    return redirect('/')



                elif svar == aj_svar and tvar == aj_tvar and aj_short == short and aj_possible == possiblequestion and aj_ckeditor == ckeditor:
                    #New_item1=Post.objects.get(sub_topic=aj_subtopic,topic=aj_topic)
                    New_item1=Post.objects.get(id=h_id)
                    New_item1.delete()
                    xmlName=BASE_DIR+'/All_contents/'+str(topic)+'/'+str(aj_subtopic)+'.xml'
                    os.system('rm "'+xmlName+'"')

                    dirName=BASE_DIR+'/All_contents/'+str(topic)
                    xmlName=BASE_DIR+'/All_contents/'+str(topic)+'/'+str(subtopic)+'.xml'

                    file2=open(str(xmlName),"w")

                    toFile1='<?xml version="1.0" encoding="UTF-8"?><Data><topic>Topic:'+str(topic)+'</topic><Variations1>'+str(tvar)+'</Variations1><Sub_topic>'+str(subtopic)+'</Sub_topic><Variations2>'+str(svar)+'</Variations2><Short_description>'+str(short)+'</Short_description><Possible_question>'+str(possiblequestion)+'</Possible_question><ckeditor>'+str(ckeditor)+'</ckeditor><image>'+str(image_list)+'</image></Data>'
            
                
                    file2.write(toFile1)
                    file2.close()
                    args=Post.objects.create(topic=topic,var1=tvar,sub_topic=str(subtopic),var2=svar,short=short,possible=possiblequestion,ck=ckeditor,image=image_list)


                    # folder_names=os.listdir(BASE_DIR +'/All_contents')
                    # dic_filenames = {}
                    # for f_name in folder_names:
                    #     new_path = BASE_DIR +"/All_contents/" + f_name
                    #     array_sub_topic1=os.listdir(new_path)
                    #     array_sub_topic2=[]

                    #     for item in array_sub_topic1:
                    #         item=item.replace('.xml','')
                    #         array_sub_topic2.append(item)
                    #     dic_filenames[f_name] = array_sub_topic2

                    #return render(request,'atoskb/first.html',{'dic_filenames':dic_filenames})
                    return redirect('/')
                else:
                    pass


        else:
            pass
    else:
        pass            




@csrf_exempt
def edit_post(request):
    #import pdb;pdb.set_trace()
    if request.is_ajax():
        item_id=request.POST.get('id')
        list_id=item_id.split('##')
        edit_topic=list_id[1]
        edit_sub_topic=list_id[0]

        New_item=Post.objects.get(topic=edit_topic,sub_topic=edit_sub_topic)
        image_value=New_item.image
        image_value=unicodedata.normalize('NFKD', image_value).encode('ascii','ignore')

        latest={'t_id':New_item.id,'Topic':str(New_item.topic),'Tvariations':str(New_item.var1),'Sub_Topic':str(New_item.sub_topic),'Svariations':str(New_item.var2),'Short_description':str(New_item.short),'possible_question':str(New_item.possible),'ckeditor':str(New_item.ck),'image':image_value}
        
        print New_item.image
        import pdb;pdb.set_trace()
    response = HttpResponse(json.dumps({'latest':latest}), content_type="application/json")
    return response
        