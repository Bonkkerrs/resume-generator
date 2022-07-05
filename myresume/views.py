from django.shortcuts import render, HttpResponse
from myresume.models import *


class SectionPackage:
    def __init__(self, section_obj, subsection_list):
        self.section = section_obj
        self.subsection_list = subsection_list


class SubsectionPackage:
    def __init__(self, subsection_obj, user_id):
        self.subsection = subsection_obj
        self.entries = Entry.objects.filter(user_id=user_id, by_subsection_id=subsection_obj.id)
        self.items = Item.objects.filter(user_id=user_id, by_subsection_id=subsection_obj.id)


# Create your views here.
def resume_display(request, id):
    user = User.objects.get(id=id)
    section_list = Section.objects.all()
    subsection_list = Subsection.objects.filter(user_id=id)
    section_list_temp = []
    for section in section_list:
        subsection_list_filtered = Subsection.objects.filter(by_section_id=section.id, user_id=id)
        subsection_list_temp = []
        for subsection_filtered in subsection_list_filtered:
            subsection_list_temp.append(SubsectionPackage(subsection_filtered, id))
        section_list_temp.append(SectionPackage(section, subsection_list_temp))
    return render(request, 'display.html', locals())
