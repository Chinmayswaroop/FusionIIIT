from django.contrib import admin

from .models import (BranchChange, CoursesMtech, FinalRegistrations, Register,
                     Thesis)

admin.site.register(Thesis)
admin.site.register(Register)
admin.site.register(FinalRegistrations)
admin.site.register(BranchChange)
admin.site.register(CoursesMtech)
