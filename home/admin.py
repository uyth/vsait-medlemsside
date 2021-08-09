from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils import timezone
from .forms import VsaitUserRegistrationForm, VsaitUserChangeForm
from .models import VsaitUser, Membership

class MembershipFilter(SimpleListFilter):
    title = 'membership'
    parameter_name = 'memberships'

    def lookups(self, request, model_admin):
        return (
            ('membership_true', 'Har medlemskap'),
            ('membership_pending', "Har ventende medlemskap "),
            ('membership_false', "Har ikke medlemskap"),
        )

    def queryset(self, request, queryset):
        this_years_membership = Membership.objects.filter(year=timezone.now().year)
        if (len(list(this_years_membership)) > 0):
            this_years_membership = this_years_membership.get().year
        else:
            this_years_membership = 2021
        query_memberships = [[y.year for y in list(x.memberships.all())] for x in list(queryset)]
        user_ids = [x.id for x in list(queryset)]
        has_membership = []
        for i in range(len(query_memberships)):
            print(this_years_membership, query_memberships[i])
            if this_years_membership in query_memberships[i]:
                has_membership.append(user_ids[i]);
        
        if self.value() == 'membership_true':
            return queryset.filter(id__in=has_membership)
        elif self.value() == 'membership_false':
            return queryset.exclude(id__in=has_membership)
        elif self.value() == 'membership_pending':
            return queryset.exclude(id__in=has_membership).filter(pending_membership=True)
        else:
            return queryset

def add_membership(modeladmin, request, queryset):
    membership = Membership.objects.filter(year=timezone.now().year).get()
    for users in queryset:
        users.memberships.add(membership);
add_membership.short_description = "Bekreft at utvalgte brukere har betalt for medlemskap "

def cancel_membership(modeladmin, request, queryset):
    membership = Membership.objects.filter(year=timezone.now().year).get()
    for users in queryset:
        users.memberships.remove(membership);
cancel_membership.short_description = "Ta vekk utvalgte brukeres medlemskap"

# https://django.readthedocs.io/en/stable/ref/contrib/admin/actions.html
# Implements the UserAdmin
class VsaitUserAdmin(UserAdmin):
    add_form = VsaitUserRegistrationForm # Add new user form
    form = VsaitUserChangeForm # Edit user form
    model = VsaitUser
    # Filtering and ordering of users, marks which tags to be shown
    search_fields = ('email',)
    ordering = ('email',)
    actions = [add_membership, cancel_membership]
    filter_horizontal = ()
    list_display = ['firstname','lastname','email','date_of_birth_display','date_joined_display','student','has_membership','is_staff']
    list_filter = ('student',MembershipFilter,'is_staff')
    # Fieldset for the user forms
    #email_confirmed = models.BooleanField(default=False)
    #secret_email_confirmation_url = models.CharField(max_length=100, default=uuid.uuid4().hex)
    #secret_password_change_url = models.CharField(max_length=100, default=uuid.uuid4().hex)
    fieldsets = (
        (None, {'fields': ('email', 'new_password')}),
        ('Personal Information', {'fields': ('firstname', 'lastname', 'date_of_birth','student','food_needs')}),
        ('Membership Information', {'fields': ('memberships','pending_membership')}),
        ('Email confirmation', {'fields': ['email_confirmed','secret_email_confirmation_url'], 'classes': ['collapse']}),
        ('Account information', {'fields': ['is_staff','is_superuser'], 'classes': ['collapse']}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password', 'password_confirmation')}),
        ('Personal Information', {'fields': ('firstname', 'lastname', 'date_of_birth','student','food_needs')}),
        ('Membership Information', {'fields': ('memberships','pending_membership',)}),
        ('Account information', {'fields': ['is_staff','is_superuser'], 'classes': ['collapse']}),
    )
admin.site.register(VsaitUser, VsaitUserAdmin)
admin.site.register(Membership)
admin.site.unregister(Group)
