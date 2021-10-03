from flask import Flask, render_template, redirect
from forms import AddCandidateForm
from forms import AddJobForm
from forms import AddCustomerForm
import logging
import logging.config
import candidateUIService
import jobUIService
import customerUIService

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dinasecretkey'

logging.config.fileConfig('logging.conf')
# create logger
logger = logging.getLogger('webapp')

@app.route("/", methods=["GET", "POST"])
def index():
    print("Home Page Loaded Successfully")

    return render_template("base.html")

@app.route("/candidate", methods=["GET", "POST"])
def candidate():
    print("Candidate Page Loaded Successfully")

    return render_template("candidate.html")

@app.route("/job", methods=["GET", "POST"])
def job():
    print("Job Page Loaded Successfully")

    return render_template("job.html")

@app.route("/customer", methods=["GET", "POST"])
def customer():
    print("Customer Page Loaded Successfully")

    return render_template("customer.html")

@app.route("/addcandidate", methods=["GET", "POST"])
def managecandidate():
    form = AddCandidateForm()
    print("Candidate Form Loaded Successfully")
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print("Add Candidate button clicked")
        print("Name is: " + form.name.data)
        candidateUIService.save_candidate(
            name=form.name.data,
            address=form.address.data,
            qualification=form.qualification.data,
            jobskill=form.jobskill.data,
            yearsofexperience=form.yearsofexperience.data)
        return render_template("candidateThankyou.html")
    return render_template("addCandidate.html", form=form)


@app.route("/listcandidates")
def listcandidates():
    allCandidatesList = candidateUIService.get_all_candidates()

    return render_template("candidateList.html", allCandidatesList=allCandidatesList)

@app.route("/addjob", methods=["GET", "POST"])
def managejob():
    form = AddJobForm()
    print("Job Form Loaded Successfully")
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print("Add Job button clicked")
        print("Client Name is: " + form.clientname.data)
        jobUIService.save_job(
            clientname=form.clientname.data,
            jobprofile=form.jobprofile.data,
            jobrequirements=form.jobrequirements.data)
        return render_template("jobThankyou.html")
    return render_template("addJob.html", form=form)

@app.route("/listjobs")
def listjobs():
    allJobsList = jobUIService.get_all_jobs()

    return render_template("jobList.html", allJobsList=allJobsList)

@app.route("/addcustomer", methods=["GET", "POST"])
def managecustomer():
    form = AddCustomerForm()
    print("Customer Form Loaded Successfully")
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print("Add Customer button clicked")
        print("Client Name is: " + form.name.data)
        customerUIService.save_customer(
            name=form.name.data,
            address=form.address.data)
        return render_template("customerThankyou.html")
    return render_template("addCustomer.html", form=form)


@app.route("/listcustomers")
def listcustomers():
    allCustomersList = customerUIService.get_all_customers()

    return render_template("customerList.html", allCustomersList=allCustomersList)

if __name__ == "__main__":
    app.run()
